# Generated by Django 4.1.2 on 2022-10-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocompletion_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
