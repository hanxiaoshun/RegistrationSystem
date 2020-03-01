# Generated by Django 2.2.2 on 2019-07-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0043_auto_20190721_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemmessage',
            name='message',
        ),
        migrations.AddField(
            model_name='systemmessage',
            name='message_content',
            field=models.TextField(default='', help_text='消息内容', max_length=500, null=True, verbose_name='消息内容'),
        ),
        migrations.AddField(
            model_name='systemmessage',
            name='message_title',
            field=models.CharField(default='', help_text='消息标题不可为空！', max_length=50, verbose_name='消息标题'),
        ),
    ]
