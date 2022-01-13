# Generated by Django 3.2.10 on 2022-01-13 00:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_participation_birth_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2022)], verbose_name='Год написания пьесы'),
        ),
    ]