# Generated by Django 4.2.17 on 2025-01-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0005_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
