# Generated by Django 2.2.2 on 2019-07-06 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20190706_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=50, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='fixed_telephone',
            field=models.CharField(blank=True, default='', help_text='固定电话（带区号）', max_length=20, null=True, verbose_name='固定电话（带区号）'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='real_name',
            field=models.CharField(default='', help_text='真实姓名', max_length=50, null=True, verbose_name='真实姓名'),
        ),
    ]
