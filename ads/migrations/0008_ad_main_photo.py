# Generated by Django 4.1.2 on 2022-10-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_remove_ad_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='main_photo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]