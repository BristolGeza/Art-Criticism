# Generated by Django 4.2.17 on 2025-01-15 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_post_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
    ]
