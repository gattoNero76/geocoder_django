# Generated by Django 2.1.2 on 2018-10-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0003_auto_20181019_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='coordinates',
            field=models.CharField(default='', max_length=300),
        ),
    ]
