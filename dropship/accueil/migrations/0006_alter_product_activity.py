# Generated by Django 4.0.5 on 2022-06-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='activity',
            field=models.BooleanField(null=True),
        ),
    ]
