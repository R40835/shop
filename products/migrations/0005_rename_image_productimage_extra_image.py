# Generated by Django 5.0.1 on 2024-02-02 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_follower_first_name_follower_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='extra_image',
        ),
    ]
