# Generated by Django 2.2.2 on 2019-07-09 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_remove_teacherinfo_user_info_working_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='person_in_charge',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='teacher_number',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='teacher_info',
            field=models.ForeignKey(blank=True, help_text='负责人基本信息', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webapp_studentinfo_TeacherInfo', to='webapp.TeacherInfo', verbose_name='负责人基本信息'),
        ),
    ]
