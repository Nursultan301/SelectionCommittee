from django.db import models


class Entrant_9(models.Model):
    GENDER = [
        ('men', 'Мужчина'),
        ('women', 'Женщина')
    ]

    fist_name = models.CharField("Фамилия", max_length=50)
    last_name = models.CharField("Имя", max_length=50)
    full_name = models.CharField("Отчество", max_length=50)
    birth_date = models.DateField("Дата рождения")
    gender = models.CharField("Пол", max_length=10, choices=GENDER, default='men')
    passport_phone = models.ImageField("Передний фото паспорта")
    passport_phone2 = models.ImageField("Задний фото паспорта")
    passport_id = models.CharField("Паспорт Id", max_length=50)
    diploma_phone = models.ImageField("Фото аттестата")
    diploma_id = models.CharField("Номер аттестата", max_length=50)

    def __str__(self):
        return f'{self.fist_name} {self.last_name}, {self.full_name}'

    class Meta:
        verbose_name = 'Абитуриент 9го класса'
        verbose_name_plural = 'Абитуриенты 9го класса'
        abstract = True


class Entrant_11(Entrant_9):
    diploma_phone2 = models.ImageField("2 фото аттестата")
