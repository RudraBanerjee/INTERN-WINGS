# Generated by Django 5.0 on 2024-01-21 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='catagory',
            new_name='Catagories',
        ),
    ]
