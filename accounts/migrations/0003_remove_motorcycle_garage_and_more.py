# Generated by Django 5.1.6 on 2025-02-24 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email_alter_customuser_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motorcycle',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='marketplacemotorcycle',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='merchandise',
            name='store',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='route',
            name='user',
        ),
        migrations.RemoveField(
            model_name='store',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='story',
            name='user',
        ),
        migrations.DeleteModel(
            name='Garage',
        ),
        migrations.DeleteModel(
            name='Motorcycle',
        ),
        migrations.DeleteModel(
            name='MarketplaceMotorcycle',
        ),
        migrations.DeleteModel(
            name='Merchandise',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
