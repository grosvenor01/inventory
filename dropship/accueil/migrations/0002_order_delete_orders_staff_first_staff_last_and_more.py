# Generated by Django 4.0.5 on 2022-06-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('quantité', models.IntegerField()),
                ('order_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.AddField(
            model_name='staff',
            name='first',
            field=models.CharField(default='anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='last',
            field=models.CharField(default='anonymous', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]