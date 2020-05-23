import django.utils.timezone as timezone
from django.db import models
import uuid


class ReportBase(models.Model):
    """
    基础信息类
    """
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_Operator",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)  
    objects = models.Manager()
