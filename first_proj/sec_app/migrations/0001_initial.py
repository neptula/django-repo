# Generated by Django 3.2.3 on 2021-06-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, unique=True)),
                ('last_name', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
