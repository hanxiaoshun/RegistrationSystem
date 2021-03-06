# Generated by Django 2.2.2 on 2019-07-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20190711_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolterm',
            name='students',
            field=models.IntegerField(default=0, help_text='本期报名的学员总数量', null=True, verbose_name='本期学员总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_chemical',
            field=models.IntegerField(default=0, help_text='本期化工学员数量', null=True, verbose_name='本期化工学员数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_chemical_not',
            field=models.IntegerField(default=0, help_text='本期非化工学员数量', null=True, verbose_name='本期非化工学员数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_confirm',
            field=models.IntegerField(default=0, help_text='本期资料确认通过的总数量', null=True, verbose_name='本期资料确认通过的总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_confirm_not',
            field=models.IntegerField(default=0, help_text='本期资料未确认通过的总数量', null=True, verbose_name='本期资料未确认通过的总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_pay',
            field=models.IntegerField(default=0, help_text='本期已缴费学员数量', null=True, verbose_name='本期已缴费学员数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_pay_not',
            field=models.IntegerField(default=0, help_text='本期未缴费学员数量', null=True, verbose_name='本期未缴费学员数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_review',
            field=models.IntegerField(default=0, help_text='本期已提交资料的学员总数量', null=True, verbose_name='本期已提交资料的学员总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_review_not',
            field=models.IntegerField(default=0, help_text='本期未提交资料的学员总数量', null=True, verbose_name='本期未提交资料的学员总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_submit',
            field=models.IntegerField(default=0, help_text='本期已提交资料的学员总数量', null=True, verbose_name='本期已提交资料的学员总数量'),
        ),
        migrations.AddField(
            model_name='schoolterm',
            name='students_submit_not',
            field=models.IntegerField(default=0, help_text='本期未提交资料的学员总数量', null=True, verbose_name='本期未提交资料的学员总数量'),
        ),
    ]
