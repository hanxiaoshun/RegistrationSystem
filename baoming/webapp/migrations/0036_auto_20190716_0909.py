# Generated by Django 2.2.2 on 2019-07-16 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0035_registeruserinfo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewaudit',
            old_name='operation_error_msg',
            new_name='operation_message',
        ),
    ]
