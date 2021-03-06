# Generated by Django 3.0.4 on 2020-04-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200403_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat_from',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat_to',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='long_from',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='long_to',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
    ]
