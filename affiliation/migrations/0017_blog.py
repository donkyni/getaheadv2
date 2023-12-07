# Generated by Django 4.2.7 on 2023-12-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliation', '0016_alter_user_pays_de_residence_alter_user_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Blog/')),
                ('titre', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('vue', models.BigIntegerField(default=0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
    ]
