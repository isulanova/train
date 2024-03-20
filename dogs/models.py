from django.db import models

class DogsTable(models.Model):
    breed = models.CharField(max_length=150, unique=True, verbose_name='Порода')
    main_img = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    appearance = models.TextField(unique=True, blank=True, null=True, verbose_name='Внешний вид')
    character = models.TextField(unique=True, blank=True, null=True, verbose_name='Характер')
    care = models.TextField(unique=True, blank=True, null=True, verbose_name='Уход')
    illness = models.TextField(unique=True, blank=True, null=True, verbose_name='Болезни')
    img_1 = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение 1')
    img_2 = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение 2')
    img_3 = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение 3')
    char_img = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение характер')
    ill_img = models.ImageField(upload_to='dogs_images', blank=True, null=True, verbose_name='Изображение болезни')

    class Meta:
        db_table = "dogstable"

    def __str__(self):
        return self.breed
    
    def display_info(self):
        info = self.appearance
        info = list(map(str, info.SplitTextField("\n")))
        return info
        


