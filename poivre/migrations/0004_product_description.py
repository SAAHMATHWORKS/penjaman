# Generated by Django 2.2 on 2020-06-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poivre', '0003_product_remise'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
