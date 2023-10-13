from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):

    title = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return f'{self.title}'

class Product(models.Model):

    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Картинка')
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
        