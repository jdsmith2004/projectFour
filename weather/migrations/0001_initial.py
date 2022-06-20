# Generated by Django 3.1.5 on 2021-11-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('sky', models.CharField(max_length=100)),
            ],
        ),
    ]
