# Generated by Django 4.2.5 on 2023-09-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_model_email_remove_model_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
