# Generated by Django 2.2.16 on 2023-01-11 22:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230106_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(regex='^[-a-zA-Z0-9_]+$')], verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, message='Р—РЅР°С‡РµРЅРёРµ РіРѕРґР° РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅС‹Рј'), django.core.validators.MaxValueValidator(2023, message='Р—РЅР°С‡РµРЅРёРµ РіРѕРґР° РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ Р±РѕР»СЊС€Рµ С‚РµРєСѓС‰РµРіРѕ')], verbose_name='Год произведения'),
        ),
    ]
