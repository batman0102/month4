# Generated by Django 5.0.4 on 2024-04-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_alter_clothes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
