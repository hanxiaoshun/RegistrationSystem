# Generated by Django 2.2.2 on 2019-07-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='work_unit',
            field=models.CharField(blank=True, help_text='工作单位信息,可为空！', max_length=100, null=True, verbose_name='工作单位'),
        ),
    ]
