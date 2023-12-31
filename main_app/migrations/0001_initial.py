# Generated by Django 4.2.4 on 2023-08-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField(verbose_name='Date Planted')),
                ('description', models.TextField(max_length=500)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
