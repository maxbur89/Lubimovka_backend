# Generated by Django 3.2.9 on 2021-12-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_data_add_mail_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.TextField(blank=True, default='', max_length=250, verbose_name='Описание настройки'),
            preserve_default=False,
        ),
    ]
