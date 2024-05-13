from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house}'


class Supplier(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название поставщика')
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Контакт')
    link = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Поставщик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания поставщика')
    debt = models.PositiveIntegerField(default=0, verbose_name='Задолженность перед поставщиком')
    level = models.PositiveIntegerField(default=0, verbose_name='Уровень иерархии поставщика')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода продукта на рынок')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Поставщик продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}, {self.model}'
