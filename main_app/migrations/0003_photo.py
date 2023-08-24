# Generated by Django 4.2.4 on 2023-08-23 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]