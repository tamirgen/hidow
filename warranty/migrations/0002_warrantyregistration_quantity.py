# Generated by Django 3.2 on 2022-07-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warrantyregistration',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]