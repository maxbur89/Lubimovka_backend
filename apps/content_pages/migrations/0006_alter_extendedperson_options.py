# Generated by Django 3.2.9 on 2021-12-10 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_pages', '0005_auto_20211205_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extendedperson',
            options={'ordering': ('order',), 'verbose_name': 'Элемент блока персон', 'verbose_name_plural': 'Элементы блоков песроны'},
        ),
    ]
