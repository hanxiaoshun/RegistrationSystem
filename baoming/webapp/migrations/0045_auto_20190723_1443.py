# Generated by Django 2.2.2 on 2019-07-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_auto_20190721_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemmessage',
            name='hidden_status',
        ),
        migrations.AddField(
            model_name='systemmessage',
            name='hidden_status_receiver',
            field=models.CharField(choices=[('1', '已隐藏'), ('2', '未隐藏')], default=2, help_text='1 已隐藏将不会显示在查看列表中 2 未隐藏将显示在查看列表中', max_length=50, verbose_name='发送人隐藏消息状态'),
        ),
        migrations.AddField(
            model_name='systemmessage',
            name='hidden_status_sender',
            field=models.CharField(choices=[('1', '已隐藏'), ('2', '未隐藏')], default=2, help_text='1 已隐藏将不会显示在查看列表中 2 未隐藏将显示在查看列表中', max_length=50, verbose_name='发送人隐藏消息状态'),
        ),
    ]