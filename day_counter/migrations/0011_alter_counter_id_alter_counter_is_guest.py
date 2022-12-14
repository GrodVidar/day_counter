# Generated by Django 4.1.1 on 2022-09-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_counter', '0010_remove_counter_name_counter_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='is_guest',
            field=models.BooleanField(default=True),
        ),
    ]
