# Generated by Django 5.0.7 on 2024-07-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to='course'),
            preserve_default=False,
        ),
    ]
