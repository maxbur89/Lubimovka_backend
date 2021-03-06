# Generated by Django 3.2.9 on 2021-11-23 22:38

from django.db import migrations


def create_role_types(apps, schema_editor):
    RoleType = apps.get_model("core", "RoleType")
    role_types = [
        {
            "role_type": "blog_persons_role",
        },
        {
            "role_type": "performanse_role",
        },
        {
            "role_type": "play_role",
        },
        {
            "role_type": "master_class_role",
        },
        {
            "role_type": "reading_role",
        },
    ]
    for type in role_types:
        type_obj, _ = RoleType.objects.get_or_create(**type)
        type_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_auto_20211207_2057"),
    ]

    operations = [migrations.RunPython(create_role_types)]
