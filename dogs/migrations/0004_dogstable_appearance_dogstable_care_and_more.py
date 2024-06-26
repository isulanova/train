# Generated by Django 4.2.7 on 2024-03-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_dogsproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogstable',
            name='appearance',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Внешний вид'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='care',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Уход'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='char_img',
            field=models.ImageField(blank=True, null=True, upload_to='dogs_images', verbose_name='Изображение характер'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='character',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Характер'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='ill_img',
            field=models.ImageField(blank=True, null=True, upload_to='dogs_images', verbose_name='Изображение болезни'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='illness',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Болезни'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='img_1',
            field=models.ImageField(blank=True, null=True, upload_to='dogs_images', verbose_name='Изображение 1'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='dogs_images', verbose_name='Изображение 2'),
        ),
        migrations.AddField(
            model_name='dogstable',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to='dogs_images', verbose_name='Изображение 3'),
        ),
        migrations.DeleteModel(
            name='DogsProperty',
        ),
    ]
