# Generated by Django 3.0.8 on 2020-08-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefabd',
            name='edited',
            field=models.BooleanField(default=True),
        ),
    ]
