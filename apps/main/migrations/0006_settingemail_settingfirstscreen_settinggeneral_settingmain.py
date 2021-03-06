# Generated by Django 3.2.9 on 2021-12-09 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingEmail',
            fields=[
            ],
            options={
                'verbose_name': 'Настройки почты',
                'verbose_name_plural': 'Настройки почты',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
        migrations.CreateModel(
            name='SettingFirstScreen',
            fields=[
            ],
            options={
                'verbose_name': 'Настройки первой страницы',
                'verbose_name_plural': 'Настройки первой страницы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
        migrations.CreateModel(
            name='SettingGeneral',
            fields=[
            ],
            options={
                'verbose_name': 'Общие настройки',
                'verbose_name_plural': 'Общие настройки',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
        migrations.CreateModel(
            name='SettingMain',
            fields=[
            ],
            options={
                'verbose_name': 'Настройки главной страницы',
                'verbose_name_plural': 'Настройки главной страницы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
    ]
