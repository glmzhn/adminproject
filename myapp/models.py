from django.db import models


class ItemCategory(models.Model):
    cat_name = models.CharField(max_length=256)
    cat_image = models.ImageField(null=True, blank=True, upload_to='item category/images/')


class Item(models.Model):
    name = models.CharField(max_length=256)
    item_image = models.ImageField(null=True, blank=True, upload_to='item/images/')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    colour = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    thickness = models.CharField(max_length=100)
    place_of_application = models.CharField(max_length=256)
