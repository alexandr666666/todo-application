# Generated by Django 5.0.3 on 2024-03-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50, verbose_name='')),
                ('text', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
    ]
