# Generated by Django 5.1.1 on 2024-11-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
    ]
