# Generated by Django 2.2.2 on 2019-06-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MI_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngs_in_progress',
            name='ordno',
            field=models.CharField(max_length=12, verbose_name='ordno'),
        ),
    ]