# Generated by Django 2.2.16 on 2023-01-21 23:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20230122_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Введенная оценка ниже допустимой. Оценка не может быть меньше 1.'), django.core.validators.MaxValueValidator(10, message='Введенная оценка выше допустимой. Оценка не может быть больше 10.')], verbose_name='Oценка'),
        ),
    ]