# Generated by Django 3.2.4 on 2021-07-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_storefront'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='product_stripe_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
