# Generated by Django 4.2.6 on 2023-10-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0002_product_category_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.CharField(default='sarah', max_length=100),
            preserve_default=False,
        ),
    ]
