# Generated by Django 3.1.2 on 2021-06-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20210607_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.IntegerField(blank=True),
        ),
    ]