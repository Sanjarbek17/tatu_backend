# Generated by Django 5.2 on 2025-04-21 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_professorprofile_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
