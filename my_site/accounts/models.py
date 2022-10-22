from django.db import models

class Users(models.Model):
    login = models.CharField('Логин', max_length=15)
    passwords = models.CharField('Пароль', max_length=20)
    rating = models.CharField('Уровень доступа', max_length = 30)

    def __str__(self):
        return self.login

