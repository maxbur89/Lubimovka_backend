# Generated by Django 3.2.9 on 2021-11-18 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0005_alter_event_url'),
        ('library', '0010_changes_requested_in_library'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterclass',
            old_name='event',
            new_name='events'
        ),
        migrations.RenameField(
            model_name='performance',
            old_name='event',
            new_name='events'
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='event',
            new_name='events'
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='events',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='masterclass',
                to='afisha.commonevent',
                verbose_name='События'
            ),
        ),
        migrations.AlterField(
            model_name='performance',
            name='events',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='performance',
                to='afisha.commonevent',
                verbose_name='События'
            ),
        ),
        migrations.AlterField(
            model_name='reading',
            name='events',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='reading',
                to='afisha.commonevent',
                verbose_name='События'
            ),
        ),
    ]
