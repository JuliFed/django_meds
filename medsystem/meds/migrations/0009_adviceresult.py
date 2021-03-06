# Generated by Django 2.0.6 on 2018-06-24 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0008_advicemessages'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdviceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=50)),
                ('period', models.IntegerField()),
                ('per_day', models.IntegerField()),
                ('dosage', models.FloatField()),
                ('advice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Advice')),
            ],
        ),
    ]
