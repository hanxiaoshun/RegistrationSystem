# Generated by Django 2.2.2 on 2019-07-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0046_systemmessage_reply_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='original_certificate_number',
            field=models.CharField(blank=True, default='', help_text='原证书编号', max_length=20, null=True, verbose_name='原证书编号'),
        ),
        migrations.AlterField(
            model_name='systemmessage',
            name='message_level',
            field=models.CharField(choices=[('1', '常规'), ('2', '预警'), ('3', '紧急')], default=1, help_text='消息级别', max_length=50, null=True, verbose_name='消息级别'),
        ),
        migrations.AlterField(
            model_name='systemmessage',
            name='message_range',
            field=models.CharField(choices=[('1', '系统公告'), ('2', '系统管理员'), ('3', '全体负责人'), ('4', '负责人'), ('5', '全体学员'), ('6', '负责人管辖全体学员'), ('7', '学员'), ('8', '单位报名负责人')], default='', help_text='消息发送范围', max_length=50, null=True, verbose_name='消息发送范围'),
        ),
    ]
