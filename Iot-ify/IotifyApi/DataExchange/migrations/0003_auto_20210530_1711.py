# Generated by Django 3.2.3 on 2021-05-30 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataExchange', '0002_auto_20210530_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='questions',
            new_name='parking',
        ),
        migrations.RenameField(
            model_name='parking',
            old_name='question_text',
            new_name='spot_1',
        ),
    ]
