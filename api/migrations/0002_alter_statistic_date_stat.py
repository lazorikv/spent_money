# Generated by Django 3.2.7 on 2021-09-30 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='date_stat',
            field=models.DateField(default=datetime.date(2021, 9, 30)),
        ),
    ]
