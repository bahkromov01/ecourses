# Generated by Django 5.0.7 on 2024-07-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='category'),
            preserve_default=False,
        ),
    ]
