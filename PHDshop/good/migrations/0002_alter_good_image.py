# Generated by Django 5.1.2 on 2024-11-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to=None),
        ),
    ]