# Generated by Django 3.2.8 on 2022-04-24 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220411_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='u_log',
            old_name='pwd',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='u_log',
            old_name='name',
            new_name='username',
        ),
    ]