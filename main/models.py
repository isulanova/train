from django.db import models

class images_data(models.Model):
    dog_image = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Фото собаки')
