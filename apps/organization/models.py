from django.db import models
from common import constants


class Entrant(models.Model):
    GENDER = [
        (constants.MEN, 'Мужчина'),
        (constants.WOMEN, 'Женщина')
    ]

    CLASSING = [
        (constants.CLASSING_9, '9 класс'),
        (constants.CLASSING_9, '11 класс')
    ]

    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    sur_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    photo = models.ImageField("Фото абитуриента", blank=True)
    birth_date = models.DateField("Дата рождения")
    classing = models.CharField("Какой класс", max_length=10, choices=CLASSING)
    gender = models.CharField("Пол", max_length=10, choices=GENDER, default=constants.MEN)
    passport_front_img = models.ImageField("Передний фото паспорта")
    passport_back_img = models.ImageField("Задний фото паспорта")
    passport_id = models.CharField("Паспорт Id", max_length=50)
    diploma_front_img = models.ImageField("Фото аттестата")
    diploma_back_img = models.ImageField("2 фото аттестата")
    diploma_id = models.CharField("Номер аттестата", max_length=50)
    active = models.BooleanField("Активный")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.classing == constants.CLASSING_9:
            self._meta.get_field('diploma_back_img').blank = True

    def __str__(self):
        return f'{self.first_name}-{self.passport_id}'

    def get_full_name(self):
        if self.sur_name:
            return f'{self.last_name} {self.first_name} {self.sur_name}'
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
