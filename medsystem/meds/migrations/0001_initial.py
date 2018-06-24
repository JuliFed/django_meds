# Generated by Django 2.0.6 on 2018-06-24 15:33

from django.db import migrations
from django.contrib.auth.models import User


def migrate_users(apps, schema_editor):
    user = User(pk=1, username="meds", is_active=True,
                is_superuser=True, is_staff=True,
                last_login="2011-09-01T13:20:30+03:00",
                email="meds@meds.ua",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('qwerty123')
    user.save()

    user = User(pk=2, username="Juli", is_active=True,
                is_superuser=False, is_staff=False,
                last_login="2011-09-01T13:20:30+03:00",
                email="juli@meds.ua",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('qwerty123')
    user.save()

    user = User(pk=3, username="Sidorov", is_active=True,
                is_superuser=False, is_staff=False,
                last_login="2011-09-01T13:20:30+03:00",
                email="sidorov@meds.ua",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('qwerty123')
    user.save()

    user = User(pk=4, username="Petrov", is_active=True,
                is_superuser=False, is_staff=False,
                last_login="2011-09-01T13:20:30+03:00",
                email="petrov@meds.ua",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('qwerty123')
    user.save()


class Migration(migrations.Migration):
    dependencies = [
    
    ]

    operations = [
        migrations.RunPython(migrate_users, migrations.RunPython.noop)
    ]
