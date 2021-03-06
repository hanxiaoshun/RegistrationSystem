# Generated by Django 2.2.2 on 2019-07-07 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_userinfo_main_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='status_pay',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='confirm_status',
            field=models.CharField(choices=[('0', '已确认'), ('1', '未确认')], default=1, help_text='0 已确认 1 未确认,一旦超级管理员确认,填报信息将最终生效,并进入缴费确认状态', max_length=50, verbose_name='检查状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='examination_status',
            field=models.CharField(choices=[('0', '已通过'), ('1', '未通过')], default=1, help_text='0 已通过 1 未通过,一旦通过,将结束这条信息的操作使命', max_length=50, verbose_name='考核状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='pay_status',
            field=models.CharField(choices=[('0', '已支付'), ('1', '未支付')], default=1, help_text='0 已支付 1 未支付,一旦支付,学员信息将进入学习状态', max_length=50, verbose_name='支付状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='record_status',
            field=models.CharField(choices=[('0', '启用'), ('1', '停用')], default=0, help_text='1-启用/2-停用', max_length=50, verbose_name='填报状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='review_status',
            field=models.CharField(choices=[('0', '已审核'), ('1', '未审核')], default=1, help_text='0 已审核 1 未审核,一旦审核,负责人将无法编辑修改,信息的操作权限将转移到上一级的系统超级管理员手中', max_length=50, verbose_name='检查状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='study_status',
            field=models.CharField(choices=[('0', '正常'), ('1', '异常')], default=0, help_text='0 正常 1 异常,异常应在备注中说明', max_length=50, verbose_name='学业状态'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='submit_status',
            field=models.CharField(choices=[('0', '已提交'), ('1', '未提交')], default=1, help_text='0 提交 1 未 提交,一旦提交,学员将无法编辑修改,信息的操作权限将转移到上一级的负责人手中,默认是未提交', max_length=50, verbose_name='提交状态'),
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('explain', models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='说明')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='生成时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user_Info_working_history', models.ManyToManyField(to='webapp.WorkingHistory')),
                ('user_info', models.ForeignKey(blank=True, help_text='学员基本信息', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webapp_teacherinfo_UserInfo', to='webapp.UserInfo', verbose_name='学员基本信息')),
                ('user_operator', models.ForeignKey(blank=True, help_text='操作用户记录', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='webapp_teacherinfo_Operator', to='webapp.RegisterUserInfo', verbose_name='操作用户')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
