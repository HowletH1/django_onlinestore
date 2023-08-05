from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name='Наименование')
    description_category = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name_category}: {self.description_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name_product = models.CharField(max_length=50, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f"{self.name_product} {self.description}" \
               f"{self.image} {self.category} {self.price}" \
               f"{self.date_of_creation} {self.last_modified_date}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
