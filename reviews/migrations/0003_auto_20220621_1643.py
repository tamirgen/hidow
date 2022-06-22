# Generated by Django 3.2 on 2022-06-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_products_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_cover',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title_upload_date',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
    ]