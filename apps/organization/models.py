from django.db import models


class Entrant(models.Model):
    GENDER = [
        ('men', 'Мужчина'),
        ('women', 'Женщина')
    ]

    GRADES = [
        ('grades_9', '9 класс'),
        ('grades_11', '11 класс')
    ]

    first_name = models.CharField("Фамилия", max_length=50)
    last_name = models.CharField("Имя", max_length=50)
    full_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    photo = models.ImageField("Фото абитуриента", blank=True)
    birth_date = models.DateField("Дата рождения")
    grades = models.CharField("Какой класс", max_length=10, choices=GRADES)
    gender = models.CharField("Пол", max_length=10, choices=GENDER, default='men')
    passport_phone = models.ImageField("Передний фото паспорта")
    passport_phone2 = models.ImageField("Задний фото паспорта")
    passport_id = models.CharField("Паспорт Id", max_length=50)
    diploma_phone = models.ImageField("Фото аттестата")
    diploma_phone2 = models.ImageField("2 фото аттестата")
    diploma_id = models.CharField("Номер аттестата", max_length=50)
    active = models.BooleanField("Активный")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.grades == 'grades_9':
            self._meta.get_field('diploma_phone2').blank = True

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.full_name}'

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
