# Generated by Django 2.2.2 on 2019-07-09 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_studentinfo_teacher_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherinfo',
            name='user_Info_working_history',
        ),
    ]