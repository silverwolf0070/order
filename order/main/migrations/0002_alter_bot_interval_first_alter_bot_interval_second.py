# Generated by Django 5.2.2 on 2025-06-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='interval_first',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bot',
            name='interval_second',
            field=models.IntegerField(),
        ),
    ]
