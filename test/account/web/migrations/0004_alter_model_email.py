# Generated by Django 4.2.5 on 2023-09-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_first_name_model_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='email',
            field=models.EmailField(default=0, max_length=50),
        ),
    ]
