# Generated by Django 4.2.17 on 2025-01-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0009_collaboraterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboraterequest',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
