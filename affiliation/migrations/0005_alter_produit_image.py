# Generated by Django 4.1.7 on 2023-11-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliation', '0004_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='produits/'),
        ),
    ]
