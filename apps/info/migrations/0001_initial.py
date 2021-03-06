# Generated by Django 3.2.7 on 2021-10-02 21:27

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_alter_person_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField(verbose_name='Дата начала фестиваля')),
                ('end_date', models.DateField(verbose_name='Дата окончания фестиваля')),
                ('description', models.CharField(max_length=200, verbose_name='Описание фестиваля')),
                ('year', models.PositiveSmallIntegerField(default=2021, unique=True, validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2500)], verbose_name='Год фестиваля')),
                ('programms', models.CharField(max_length=10, verbose_name='Программы фестиваля')),
                ('plays_count', models.PositiveIntegerField(default=1, verbose_name='Общее количество пьес')),
                ('selected_plays_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество отобранных пьес')),
                ('selectors_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество отборщиков пьес')),
                ('volunteers_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество волонтёров фестиваля')),
                ('events_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество событий фестиваля')),
                ('cities_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество учавствующих городов')),
                ('video_link', models.URLField(max_length=250, verbose_name='Ссылка на видео о фестивале')),
                ('blog_entries', models.CharField(max_length=10, verbose_name='Записи в блоге о фестивале')),
            ],
            options={
                'verbose_name': 'Фестиваль',
                'verbose_name_plural': 'Фестивали',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='FestivalTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('team', models.SmallIntegerField(choices=[(1, 'Арт-дирекция фестиваля'), (2, 'Команда фестиваля')], verbose_name='Тип команды')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Команда фестиваля',
                'verbose_name_plural': 'Команды фестиваля',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('type', models.CharField(choices=[(1, 'Генеральный партнер'), (2, 'Партнер фестиваля'), (3, 'Информационный партнер')], max_length=2, verbose_name='Тип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
                ('picture', models.ImageField(upload_to='images/info/partnerslogo', verbose_name='Логотип')),
                ('image', models.CharField(max_length=200, verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('map_link', models.URLField(verbose_name='Ссылка на карту')),
            ],
            options={
                'verbose_name': 'Площадка',
                'verbose_name_plural': 'Площадки',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=500, verbose_name='Текст вопроса')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=50, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Вопрос или предложение',
                'verbose_name_plural': 'Вопросы или предложения',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('year', models.PositiveSmallIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2500)], verbose_name='Год участия в фестивале')),
                ('review', models.TextField(verbose_name='Текст отзыва')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек')),
            ],
            options={
                'verbose_name': 'Волонтёр фестиваля',
                'verbose_name_plural': 'Волонтёры фестиваля',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек')),
            ],
            options={
                'verbose_name': 'Попечитель фестиваля',
                'verbose_name_plural': 'Попечители фестиваля',
            },
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(fields=('name', 'city'), name='unique_place'),
        ),
        migrations.AddField(
            model_name='festivalteam',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек'),
        ),
        migrations.AddField(
            model_name='festival',
            name='images',
            field=models.ManyToManyField(related_name='festivalimages', to='core.Image', verbose_name='Изображения'),
        ),
        migrations.AddField(
            model_name='festival',
            name='sponsors',
            field=models.ManyToManyField(related_name='festivalsponsors', to='info.Sponsor', verbose_name='Попечители фестиваля'),
        ),
        migrations.AddField(
            model_name='festival',
            name='teams',
            field=models.ManyToManyField(related_name='festivalteams', to='info.FestivalTeam', verbose_name='Арт-дирекция и команда'),
        ),
        migrations.AddField(
            model_name='festival',
            name='volunteers',
            field=models.ManyToManyField(related_name='volunteers', to='info.Volunteer', verbose_name='Волонтёры фестиваля'),
        ),
        migrations.AddConstraint(
            model_name='volunteer',
            constraint=models.UniqueConstraint(fields=('person', 'year'), name='unique_volunteer'),
        ),
        migrations.AddConstraint(
            model_name='festivalteam',
            constraint=models.UniqueConstraint(fields=('person', 'team'), name='unique_person_team'),
        ),
    ]
