# Generated by Django 2.2 on 2020-06-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poivre', '0006_product_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='produit', max_length=100),
            preserve_default=False,
        ),
    ]