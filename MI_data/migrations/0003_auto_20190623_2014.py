# Generated by Django 2.2.2 on 2019-06-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MI_data', '0002_auto_20190623_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngs_in_progress',
            name='name_fullname',
            field=models.TextField(verbose_name='Patient Name'),
        ),
    ]
