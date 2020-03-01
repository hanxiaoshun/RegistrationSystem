# Generated by Django 2.2.2 on 2019-08-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0049_auto_20190802_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='former_occupation',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='former_occupation',
            field=models.CharField(blank=True, help_text='证书本职业（工种）或相关职业（工种）', max_length=20, null=True, verbose_name='证书本职业（工种）或相关职业（工种）'),
        ),
    ]