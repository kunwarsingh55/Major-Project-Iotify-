# Generated by Django 3.2.3 on 2021-05-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataExchange', '0003_auto_20210530_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='spot_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='parking',
            name='spot_3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='parking',
            name='spot_1',
            field=models.CharField(default='', max_length=200),
        ),
    ]
