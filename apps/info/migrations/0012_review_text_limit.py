# Generated by Django 3.2.11 on 2022-01-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20220113_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='review_text',
            field=models.TextField(max_length=500, verbose_name='Текст отзыва'),
        ),
    ]