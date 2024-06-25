from django.db import models


class ItemCategory(models.Model):
    cat_name = models.CharField(max_length=256, verbose_name='Наименование категории')
    cat_image = models.ImageField(null=True, blank=True, upload_to='item category/images/',
                                  verbose_name='Изображение категории')

    def __str__(self):
        return self.cat_name


class Item(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование товара')
    item_image1 = models.ImageField(null=True, blank=True, upload_to='item/images/', verbose_name='Изображение 1')
    item_image2 = models.ImageField(null=True, blank=True, upload_to='item/images/', verbose_name='Изображение 2')
    item_image3 = models.ImageField(null=True, blank=True, upload_to='item/images/', verbose_name='Изображение 3')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name='Категория')
    colour = models.CharField(max_length=100, verbose_name='Цвет')
    material = models.CharField(max_length=100, verbose_name='Материал')
    size = models.CharField(max_length=100, verbose_name='Размер')
    thickness = models.CharField(max_length=100, verbose_name='Толщина')
    place_of_application = models.CharField(max_length=256, verbose_name='Место применения')

    def __str__(self):
        return self.name
