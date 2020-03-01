# Generated by Django 2.2.2 on 2019-07-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_studentinfo_cancel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='cancel_result',
            field=models.CharField(choices=[('0', '申请撤销成功'), ('1', '申请撤销失败')], default=1, help_text='0 申请撤销成功 1 申请撤销失败,一旦负责人同意撤销,负责人将无法编辑修改,信息的操作权限将转移到下一级的学员手中', max_length=50, verbose_name='提交撤销状态'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='cancel_status',
            field=models.CharField(choices=[('0', '申请撤销'), ('1', '未申请撤销')], default=1, help_text='0 申请撤销 1 未申请撤销,一旦申请被受理,学员将无法编辑修改,信息的操作权限将转移到上一级的负责人手中', max_length=50, verbose_name='是否提交注销申请'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='confirm_status',
            field=models.CharField(choices=[('0', '已确认'), ('1', '未确认')], default=1, help_text='0 已确认 1 未确认,一旦超级管理员确认,填报信息将最终生效,并进入缴费确认状态，学员将无法提交注销申请！', max_length=50, verbose_name='检查状态'),
        ),
    ]
