# Generated by Django 2.0.6 on 2018-06-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_sprservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
