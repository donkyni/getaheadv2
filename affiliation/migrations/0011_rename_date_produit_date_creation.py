# Generated by Django 4.2.7 on 2023-11-29 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliation', '0010_alter_produit_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='date',
            new_name='date_creation',
        ),
    ]
