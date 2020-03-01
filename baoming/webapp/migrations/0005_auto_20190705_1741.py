# Generated by Django 2.2.2 on 2019-07-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190705_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(help_text='常住住址', max_length=200, null=True, verbose_name='常住住址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id_card_address',
            field=models.CharField(help_text='身份证住址', max_length=200, null=True, verbose_name='身份证住址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='working_year',
            field=models.SmallIntegerField(default=0, help_text='小于10个月，默认为小数年。如果大于10个月约等于1年', null=True, verbose_name='参加工作年限'),
        ),
    ]
