# Generated by Django 4.1.2 on 2022-10-10 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autocompletion_app', '0002_alter_words_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='words',
            table='word_table',
        ),
    ]
