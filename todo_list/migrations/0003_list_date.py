# Generated by Django 2.1.7 on 2019-03-14 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_remove_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
