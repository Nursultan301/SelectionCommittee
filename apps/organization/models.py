from django.db import models
from common import constants


class Specialty(models.Model):
    """Специальность"""
    FORM_STATUS = (
        (constants.FULL_PART_TIME, 'Очный / Заочный'),
        (constants.FULL_TIME, 'Очный')
    )
    BASIC_STATUS = (
        (constants.CONTRACT, 'Контракт'),
        (constants.BUDGET_CONTRACT, 'Бюджет / Контракт')
    )
    number = models.IntegerField('Шифр', null=True, blank=True)
    title = models.CharField('Название', max_length=100)
    cipher = models.CharField('Регистрационный Шифр', max_length=20)

    form_training = models.CharField('Форма обучение', max_length=20, choices=FORM_STATUS, default='full_time')
    basic_training = models.CharField('Основа обучение', max_length=20, choices=BASIC_STATUS, default='contract')

    def get_full_name(self):
        """Полное имя абитуриента"""
        return f"{self.number} {self.title}"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Entrant(models.Model):
    """Заявления"""
    CLASS = (
        (constants.CLASSING_9, '9 класс'),
        (constants.CLASSING_11, '11 класс')
    )
    AREA = (
        (constants.BATKEN, 'Баткен'),
        (constants.DJALAL_ABAD, 'Джалал-Абад'),
        (constants.ISSYK_KUL, 'Иссык-куль'),
        (constants.NARYN, 'Нарын'),
        (constants.OSH, 'Ош'),
        (constants.TALAS, 'Талас'),
        (constants.CHYI, 'Чуй'),
        (constants.BISHKEK, 'Бишкек'),
    )
    NATIONALITY = (
        (constants.KYRGYZ, 'Кыргыз'),
        (constants.RUSSIAN, 'Русский'),
        (constants.KAZAKH, 'Казах'),
        (constants.UZBEK, 'Узбек'),
        (constants.TAJIK, 'Таджик'),
        (constants.OTHER, 'Другое'),
    )
    GENDER_STATUS = (
        (constants.MEN, 'Мужчина'),
        (constants.WOMEN, 'Женщина')
    )
    FORM_STATUS = (
        (constants.FULL_TIME, 'Очный'),
        (constants.PART_TIME, 'Заочный')
    )
    BASIC_STATUS = (
        (constants.BUDGET, 'Бюджет'),
        (constants.CONTRACT, 'Контракт')
    )
    STATUS = (
        (constants.RENDING_REVIEW, 'В ожидании рассмотрения'),
        (constants.APPROVE, 'Одобрен'),
        (constants.REJECT, 'Отклонён'),
    )

    serial_number = models.IntegerField(verbose_name='Порядковый номер', null=True, blank=True)
    registration_number = models.CharField('Регистрационный номер', max_length=30, null=True, blank=True,
                                           default='None')
    number = models.CharField('Номер заявки', max_length=20, default=0)
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    sur_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    area = models.CharField('Область', max_length=70, choices=AREA)
    base_class = models.CharField('На базе', max_length=25, choices=CLASS)
    certificate_number = models.CharField('Серия и номер (свидетельство или аттестат)', max_length=50, unique=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    nationality = models.CharField('Национальность', max_length=50, choices=NATIONALITY)
    gender = models.CharField(verbose_name='Пол', max_length=10, choices=GENDER_STATUS)
    form_training = models.CharField('Форма обучение', max_length=10, choices=FORM_STATUS)
    basic_training = models.CharField('Основа обучение', max_length=10, choices=BASIC_STATUS, default='9')
    specialty = models.ForeignKey(Specialty, verbose_name='Специальность', on_delete=models.PROTECT,
                                  related_name='statements')
    father = models.CharField('Отец', max_length=100)
    father_phone = models.CharField('Номер телефона', max_length=50)
    mother = models.CharField('Мать', max_length=100)
    mother_phone = models.CharField('Номер телефона', max_length=50)
    place_of_residence = models.CharField('Место жительство студента', max_length=150)
    phone_student = models.CharField('Номер телефона студента', max_length=50)

    image_passport_frond = models.ImageField(verbose_name='Передняя сторона паспорта или свидетельство о рождении',
                                             upload_to='upload_to_passport/')
    image_passport_back = models.ImageField(verbose_name='Задняя сторона паспорта или свидетельство о рождении',
                                            upload_to='upload_to_passport/')
    passport_document_number = models.CharField('Номер документа', max_length=20, help_text="ID12344567")
    image_certificate_page_1 = models.ImageField(
        verbose_name='Передняя сторона аттестата или свидетельство о образовании',
        upload_to='upload_to_certificate/')
    image_certificate_page_2 = models.ImageField(verbose_name='Задняя сторона аттестата или свидетельство о образовании',
                                               upload_to='upload_to_certificate/')

    status = models.CharField('Статус', max_length=40, choices=STATUS, default='В ожидании рассмотрения')

    updated = models.DateTimeField(auto_now=True)  # -- Дата обновлении
    created = models.DateTimeField(auto_now_add=True)  # -- Дата создание заявление

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.base_class == constants.CLASSING_9:
            self._meta.get_field('image_certificate_page_2').blank = True
            self._meta.get_field('image_certificate_page_2').null = True

    def __str__(self):
        return f"{self.first_name} - {self.passport_document_number}"

    def get_full_name(self):
        if self.sur_name:
            return f'{self.last_name} {self.first_name} {self.sur_name}'
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
