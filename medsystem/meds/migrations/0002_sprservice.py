# Generated by Django 2.0.6 on 2018-06-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SprService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
