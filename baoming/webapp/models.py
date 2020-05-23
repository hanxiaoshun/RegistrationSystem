# -*- coding: UTF-8 -*-
import django.utils.timezone as timezone
from django.db import models
import uuid

# class models.Model(models.Model):
#     """
#     公共字段信息，操作人，操作时间、修改时间
#     """
#     explain = models.TextField('说明', default='', max_length=200, blank=True)
#     user_operator = models.ForeignKey('self', to_field='id',
#                                       related_name="%(app_label)s_%(class)s_操作用户",
#                                       verbose_name='操作人',
#                                       blank=True,
#                                       null=True,
#                                       on_delete=models.SET_NULL,
#                                       help_text='操作人记录')
#     create_time = models.DateTimeField('生成时间', default=timezone.now)
#     modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
#
#     class Meta:
#         abstract = True


class ProvinceCityCountry(models.Model):
    """
    省市县信息汇总表，新增编码
    """
    id = models.AutoField('区域ID', primary_key=True)
    region_name = models.CharField('区域名称', max_length=50, help_text='区域名称', default='', blank=False)
    region_ID = models.CharField('区域ID(手动)', max_length=50, help_text='区域名称', default='', blank=False)
    region_code = models.CharField('区域编码', max_length=50, help_text='区域名称', default='', blank=False)
    parent = models.ForeignKey('self', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    zipcode = models.CharField('邮编', max_length=50, help_text='邮编', default="", blank=False)
    region_level = models.CharField('区域等级', max_length=10, help_text='0~5,省市县镇乡村', default=99,
                                    choices=[('0', '省级'),
                                             ('1', '市级'),
                                             ('2', '县级'),
                                             ('3', '镇级'),
                                             ('4', '乡级'),
                                             ('5', '村级'),
                                             ('99', '未分级')])
    region_status = models.CharField('区域使用状态', max_length=10, help_text='0 正常使用，1 未正常使用',
                                     choices=[('0', '正常使用'),
                                              ('1', '未正常使用')])
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '省市县信息汇总表'
        verbose_name_plural = '省市县信息汇总表'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.region_name


class EducationDegree(models.Model):
    """
    学历信息管理
    """
    id = models.AutoField('学历ID', primary_key=True)
    education_name = models.CharField('学历名称', max_length=50, unique=True, null=False, help_text='学历级别的分类')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '学历信息管理'
        verbose_name_plural = '学历信息管理'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.education_name


class UnitNature(models.Model):
    """
    单位性质管理
    """
    id = models.AutoField('学历ID', primary_key=True)
    unit_nature = models.CharField('单位性质名称', max_length=50, unique=True, null=False, help_text='学历级别的分类')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '单位性质管理'
        verbose_name_plural = '单位性质管理'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.unit_nature


class Picture(models.Model):
    """
    系统图片管理表
    """
    id = models.AutoField(primary_key=True, blank=False, verbose_name='图片ID')
    picture_uuid = models.UUIDField(verbose_name="图片UUID", default=uuid.uuid4, null=False, help_text="图片的唯一标识")
    picture_name = models.CharField(verbose_name="图片名称", default='未说明', max_length=50, null=True, blank=True)
    picture_path = models.ImageField("图片路径", upload_to='images/%Y/%m', max_length=200)
    main_picture = models.BooleanField(default=False, verbose_name='是否为代表性图片')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()
    class Meta:
        ordering = ['id']
        verbose_name = '系统图片管理表'
        verbose_name_plural = '系统图片管理表'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.picture_name

class IDCardPicture(models.Model):
    """
    系统(身份证件)图片管理表
    """
    id = models.AutoField(primary_key=True, blank=False, verbose_name='图片ID')
    picture_uuid = models.UUIDField(verbose_name="图片UUID", default=uuid.uuid4, null=False, help_text="图片的唯一标识")
    picture_name = models.CharField(verbose_name="图片名称", default='未说明', max_length=50, null=True, blank=True)
    picture_path = models.ImageField("图片路径", upload_to='images/%Y/%m', max_length=200)
    main_picture = models.BooleanField(default=False, verbose_name='是否为代表性图片')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()
    class Meta:
        ordering = ['id']
        verbose_name = '系统(身份证件)图片管理表'
        verbose_name_plural = '系统(身份证件)图片管理表'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.picture_name
        
        
class FileManage(models.Model):
    """
    文件管理表
    """
    id = models.AutoField(primary_key=True, blank=False, verbose_name='图片ID')
    file_uuid = models.UUIDField(verbose_name="文件UUID", default=uuid.uuid4, null=False, help_text="文件的唯一标识")
    file_name = models.CharField(verbose_name="图片名称", default='未说明', max_length=50, null=True, blank=True)
    file_path = models.CharField("文件路径", default="", max_length=500)
    file_status = models.BooleanField(default=True, verbose_name='文件是否存在')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()
    class Meta:
        ordering = ['id']
        verbose_name = '文件管理表'
        verbose_name_plural = '文件管理表'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.file_name


class WorkingHistory(models.Model):
    """
    工作年限证明
    """
    id = models.AutoField('用户ID', primary_key=True)
    start_year = models.SmallIntegerField('起始年')
    start_month = models.SmallIntegerField('起始月')
    end_year = models.SmallIntegerField('结束年')
    end_month = models.SmallIntegerField('结束月')
    unit_name = models.CharField(verbose_name='单位名称', default='', max_length=50, blank=False,
                                 help_text='单位名称')
    city_or_county = models.ForeignKey(ProvinceCityCountry,
                                       on_delete=models.SET_NULL,
                                       related_name='city_or_country',
                                       null=True,
                                       verbose_name='单位所在市（或县）',
                                       help_text='单位所在市（或县）')
    job_content = models.CharField(verbose_name='从事何种岗位工作', default='', max_length=50,
                                   help_text='从事何种岗位工作')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()
    class Meta:
        ordering = ['id']
        verbose_name = '工作年限证明'
        verbose_name_plural = '工作年限证明'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.unit_name


class AuthorityMenu(models.Model):
    """ 权限菜单 """
    id = models.AutoField('权限ID', primary_key=True)
    authority_name = models.CharField('权限名称', default='', max_length=50)
    parent = models.ForeignKey('self', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '权限菜单'
        verbose_name_plural = '权限菜单'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.authority_name


class RoleInfo(models.Model):
    """ 角色设置 """
    id = models.AutoField('角色ID', primary_key=True)
    role_name = models.CharField('角色名称（英文）', default='', max_length=50)
    role_alias = models.CharField('角色别名（中文）', default='', max_length=50)
    parent = models.ForeignKey('self', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    authorities = models.ManyToManyField(AuthorityMenu, through='RoleAuthority', through_fields=('role', 'authority'))
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '角色设置'
        verbose_name_plural = '角色设置'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.role_name


class UserRole(models.Model):
    """ 用户除了角色限定以外的特殊权限 """
    id = models.AutoField('用户角色ID', primary_key=True)
    role = models.ForeignKey('RoleInfo', to_field='id', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey('RegisterUserInfo', to_field='id', on_delete=models.CASCADE, default=None)
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        unique_together = ("user", "role")
        verbose_name = '用户角色外特权'
        verbose_name_plural = '用户角色外特权'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)


class UserAuthority(models.Model):
    """ 用户除了角色限定以外的特殊权限 """
    id = models.AutoField('用户权限ID', primary_key=True)
    authority = models.ForeignKey('AuthorityMenu', to_field='id', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey('UserInfo', to_field='id', on_delete=models.CASCADE, default=None)
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    # 使用Model.save()来更新才会更新注意
    class Meta:
        ordering = ['id']
        unique_together = ("user", "authority")
        verbose_name = '用户特定权限'
        verbose_name_plural = '用户特定权限'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)


class NationInfo(models.Model):
    """
    民族类别管理
    """
    id = models.AutoField('民族类别ID', primary_key=True)
    nation_name = models.CharField("民族类别名称", help_text="民族类别名称", max_length=30, default="", blank=False)
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '民族类别管理'
        verbose_name_plural = '民族类别管理'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.nation_name


class RoleAuthority(models.Model):
    """ 角色对应限定以外的特殊权限 """
    id = models.AutoField('角色权限ID', primary_key=True)
    role = models.ForeignKey('RoleInfo', to_field='id', on_delete=models.CASCADE, default=None)
    authority = models.ForeignKey('AuthorityMenu', to_field='id', on_delete=models.CASCADE, default=None)
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        unique_together = ("role", "authority")
        verbose_name = '角色对应限定以外的特殊权限'
        verbose_name_plural = '角色对应限定以外的特殊权限'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)


class RegisterUserInfo(models.Model):
    """
    系统注册用户基础信息
    """
    id = models.AutoField('用户ID', primary_key=True)
    username = models.CharField(verbose_name='用户名', default='', max_length=50, unique=True, blank=False,
                                help_text='用户登录所需账号')
    nickname = models.CharField('昵称', default='', max_length=50, unique=True)
    password = models.CharField('用户登录所需密码', default='', max_length=300, blank=False, help_text='用户登录所需密码')
    role = models.ForeignKey('RoleInfo', to_field='id', on_delete=models.SET_NULL,
                             related_name='RoleInfo_RegisterUserInfo', null=True, blank=True)
    status = models.CharField('注册用户的状态', max_length=50, default=1,
                              choices=[('1', '启用'),
                                       ('2', '停用')],
                              help_text='1-启用/2-停用')
    # roles = models.ManyToManyField(RoleInfo, through='UserRole', through_fields=['user', 'role'])
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '系统注册用户基础信息'
        verbose_name_plural = '系统注册用户基础信息'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.username


class UserInfo(models.Model):
    """
    注册用户详细信息
    """
    id = models.AutoField('用户ID', primary_key=True)
    register_user_info = models.ForeignKey(RegisterUserInfo,
                                           to_field='id',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,
                                           related_name='RegisterUserInfo_UserInfo',
                                           verbose_name='注册信息',
                                           help_text='注册信息')
    real_name = models.CharField(verbose_name='真实姓名', default='', max_length=50, blank=False, null=True,
                                 help_text="真实姓名")
    sex = models.CharField('性别', default='OTHER', max_length=50, choices=[('MALE', '男'),
                                                                          ('FEMALE', '女'),
                                                                          ('OTHER', '未填写')])
    age = models.SmallIntegerField('年龄', default=0, help_text='年龄', blank=True, null=True)
    fixed_telephone = models.CharField("固定电话（带区号）", max_length=20, default='', null=True, help_text='固定电话（带区号）',
                                       blank=True)
    unit_address = models.CharField("单位地址", max_length=200, default='', help_text="单位地址", null=True, blank=True)
    email = models.EmailField('邮箱', default='', max_length=50, blank=True, null=True)
    # phone = models.CharField('手机', default='', max_length=50, unique=True, blank=True) # 联系方式留一下就可以了
    birthday = models.DateField('生日', blank=True, null=True)
    status = models.CharField('用户状态', max_length=50, default=1,
                              choices=[('1', '启用'),
                                       ('2', '停用')],
                              help_text='1-启用/2-停用')
    middle_school = models.CharField("初级中学名称", max_length=200, default='', null=True, help_text="初级中学名称", blank=True)
    # 学历信息
    education_degree = models.ForeignKey(EducationDegree,
                                         on_delete=models.SET_NULL,
                                         related_name='EducationDegree_StudentInfo',
                                         null=True,
                                         blank=True,
                                         verbose_name='学历信息',
                                         help_text='学历信息')
    # 二寸照片
    two_inch_photo = models.ForeignKey(Picture,
                                       on_delete=models.SET_NULL,
                                       related_name='Picture_UserInfo',
                                       null=True,
                                       blank=True,
                                       verbose_name='二寸证件照片信息',
                                       help_text='二寸证件照片信息')
    id_number = models.CharField('身份证件号码', max_length=20, null=True, blank=True, default='', help_text='身份证件号码信息')
    work_unit = models.CharField('工作单位', max_length=100, null=True, blank=True, default='', help_text='工作单位信息,可为空！')
    unit_nature = models.ForeignKey(UnitNature,
                                    on_delete=models.SET_NULL,
                                    related_name='UnitNature_UserInfo',
                                    null=True,
                                    blank=True,
                                    verbose_name='单位性质信息',
                                    help_text='单位性质信息')

    contact_number = models.CharField('联系电话', max_length=50, blank=True, null=True, default='', help_text='联系电话')
    start_working_date = models.DateField('起始工作时间', help_text='起始工作时间,不用职位分类', null=True, blank=True)
    main_occupation = models.CharField('从事职业', max_length=50, blank=True, null=True, default='', help_text='从事职业')

    hukou_province = models.ForeignKey(ProvinceCityCountry,
                                       on_delete=models.SET_NULL,
                                       related_name='province_UserInfo',
                                       null=True,
                                       blank=True,
                                       verbose_name='省信息ID',
                                       help_text='省信息ID')
    hukou_city = models.ForeignKey(ProvinceCityCountry,
                                   on_delete=models.SET_NULL,
                                   related_name='city_UserInfo',
                                   null=True,
                                   blank=True,
                                   verbose_name='市信息ID',
                                   help_text='市信息ID')
    hukou_county = models.ForeignKey(ProvinceCityCountry,
                                     on_delete=models.SET_NULL,
                                     related_name='country_UserInfo',
                                     null=True,
                                     blank=True,
                                     verbose_name='县信息ID',
                                     help_text='县信息ID')
    nation_info = models.ForeignKey(NationInfo,
                                    on_delete=models.SET_NULL,
                                    related_name='NationInfo_UserInfo',
                                    null=True,
                                    blank=True,
                                    verbose_name='民族信息',
                                    help_text='民族信息')
    working_year = models.SmallIntegerField('参加工作年限', default=0, blank=True, null=True,
                                            help_text='小于10个月，默认为小数年。如果大于10个月约等于1年')
    address = models.CharField('常住住址', max_length=200, null=True, blank=True, default='', help_text='常住住址')
    id_card_address = models.CharField('身份证住址', max_length=200, null=True, blank=True, default='', help_text='身份证住址')
    postal_code = models.CharField('邮政编码', max_length=20, null=True, blank=True, default='', help_text='邮政编码')
    political_status = models.CharField('政治面貌', max_length=20, null=True, blank=True,
                                        help_text='政治面貌:01 中共党员,'
                                                  '02 中共预备党员,03共青团员,'
                                                  '04民革党员,05民盟盟员,06民建会员,'
                                                  '07民进会员,08农工党党员, 09致公党党员,'
                                                  '10九三学社社员,11台盟盟员,12无党派人士,'
                                                  '13群众（现称普通居民，与居民身份证相对应）',
                                        default=12,
                                        choices=[('0', '中共党员'),
                                                 ('1', '中共预备党员'),
                                                 ('2', '共青团员'),
                                                 ('3', '民革党员'),
                                                 ('4', '民盟盟员'),
                                                 ('5', '民建会员'),
                                                 ('6', '民进会员'),
                                                 ('7', '农工党党员'),
                                                 ('8', '致公党党员'),
                                                 ('9', '九三学社社员'),
                                                 ('10', '台盟盟员'),
                                                 ('11', '无党派人士'),
                                                 ('12', '群众(普通居民)')])
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    user_Info_working_history = models.ManyToManyField(WorkingHistory)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '注册用户详细信息'
        verbose_name_plural = '注册用户详细信息'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.real_name


class SchoolTerm(models.Model):
    """
    学期设置管理类
    """
    id = models.AutoField('学期ID', primary_key=True, default=None)
    school_term_name = models.CharField('学期名字', max_length=50, null=True, blank=True, default='', help_text='学期名字')
    status = models.CharField('报名系统状态', max_length=50, default=1,
                              choices=[('1', '启用'),
                                       ('2', '停用')],
                              help_text='1-启用/2-停用')
    school_term_start = models.DateField('新学期开始时间', help_text='学期开始时间，只有到了新学期时间到才能报名', null=True, blank=True)
    school_term_end = models.DateField('新学期开始时间', help_text='起始工作时间,新学期结束系统无法报名', null=True, blank=True)
    students = models.IntegerField('本期学员总数量', default=0, null=True, help_text='本期报名的学员总数量')
    students_chemical = models.IntegerField('本期化工学员数量', default=0, null=True, help_text='本期化工学员数量')
    students_chemical_not = models.IntegerField('本期非化工学员数量', default=0, null=True, help_text='本期非化工学员数量')
    students_submit = models.IntegerField('本期已提交资料的学员总数量', default=0, null=True, help_text='本期已提交资料的学员总数量')
    students_submit_not = models.IntegerField('本期未提交资料的学员总数量', default=0, null=True, help_text='本期未提交资料的学员总数量')
    students_review = models.IntegerField('本期已提交资料的学员总数量', default=0, null=True, help_text='本期已提交资料的学员总数量')
    students_review_not = models.IntegerField('本期未提交资料的学员总数量', default=0, null=True, help_text='本期未提交资料的学员总数量')
    students_confirm = models.IntegerField('本期资料确认通过的总数量', default=0, null=True, help_text='本期资料确认通过的总数量')
    students_confirm_not = models.IntegerField('本期资料未确认通过的总数量', default=0, null=True, help_text='本期资料未确认通过的总数量')
    students_pay = models.IntegerField('本期已缴费学员数量', default=0, null=True, help_text='本期已缴费学员数量')
    students_pay_not = models.IntegerField('本期未缴费学员数量', default=0, null=True, help_text='本期未缴费学员数量')
    students_status_yes = models.IntegerField('本期处于正常状态的学员', default=0, null=True, help_text='本期处于正常状态的学员')
    students_status_not = models.IntegerField('本期处于异常状态的学员', default=0, null=True, help_text='本期处于异常状态的学员')
    user_info = models.ForeignKey('UserInfo', to_field='id',
                                  related_name="%(app_label)s_%(class)s_UserInfo",
                                  verbose_name='学员基本信息',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  help_text='学员基本信息')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '学期设置管理类'
        verbose_name_plural = '学期设置管理类'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.school_term_name


class TeacherInfo(models.Model):
    """
    老师(负责人)基本信息
    """
    id = models.AutoField('用户ID', primary_key=True, default=None)
    number = models.CharField('教师编号', max_length=50, null=True, blank=True, default='', help_text='教师编号')
    user_info = models.ForeignKey('UserInfo', to_field='id',
                                  related_name="%(app_label)s_%(class)s_UserInfo",
                                  verbose_name='学员基本信息',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  help_text='学员基本信息')
    explain = models.TextField('说明', default='', max_length=200, blank=True, null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    status = models.CharField('负责人状态', max_length=50, default=1,
                              choices=[('1', '启用'),
                                       ('2', '停用')],
                              help_text='1-启用/2-停用')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '老师(负责人)基本信息'
        verbose_name_plural = '老师(负责人)基本信息'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)


class StudentInfo(models.Model):
    """
    学生填报详细信息
    """
    id = models.AutoField('用户ID', primary_key=True, default=None)
    user_info = models.ForeignKey('UserInfo', to_field='id',
                                  related_name="%(app_label)s_%(class)s_UserInfo",
                                  verbose_name='学员基本信息',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  help_text='学员基本信息')
    teacher_info = models.ForeignKey('TeacherInfo', to_field='id',
                                     related_name="%(app_label)s_%(class)s_TeacherInfo",
                                     verbose_name='负责人基本信息',
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     help_text='负责人基本信息')

    school_term = models.ForeignKey('SchoolTerm', to_field='id',
                                    related_name="%(app_label)s_%(class)s_TeacherInfo",
                                    verbose_name='负责人基本信息',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='负责人基本信息')

    hold_qualification_certificate_or_not = models.CharField('是否持有资格证件', max_length=20, null=True, blank=True,
                                                             help_text='是否持有资格证件', default=0,
                                                             choices=[('0', '持有'),
                                                                      ('1', '未持有')])
    # 原资格证书照片
    certificate_photos = models.ForeignKey(Picture,
                                           on_delete=models.SET_NULL,
                                           related_name='Certificate_Photos_StudentInfo',
                                           null=True,
                                           verbose_name='原资格证书照片',
                                           help_text='原资格证书照片')
    # 院校毕业证件照片
    diploma_certificate_photos = models.ForeignKey(Picture,
                                                   on_delete=models.SET_NULL,
                                                   related_name='Diploma_Certificate_Photos_StudentInfo',
                                                   null=True,
                                                   verbose_name='院校毕业证件照片',
                                                   help_text='院校毕业证件照片')

    profession = models.CharField('从事职业(专业工种)', max_length=50, blank=True, null=True, help_text='从事职业(专业工种，单一种类)')

    former_occupation = models.CharField('证书本职业（工种）或相关职业（工种）', max_length=20, null=True, blank=True,
                                         help_text='证书本职业（工种）或相关职业（工种）')
    primary_level = models.CharField('原级别', max_length=20, null=True, blank=True, help_text='原级别', default=99,
                                     choices=[('1', '高级技工'),
                                              ('2', '技工'),
                                              ('3', '高级'),
                                              ('4', '中级'),
                                              ('5', '初级'),
                                              ('99', '无级别信息')])
    original_certificate_number = models.CharField('原证书编号', max_length=20, default='', null=True, blank=True,
                                                   help_text='原证书编号')
    issue_unit = models.CharField("职业资格证书发行单位", max_length=100, default='', null=True, help_text='职业资格证书发行单位')
    issuance_time = models.DateField('原职业资格证发放时间', null=True, blank=True)
    start_the_work_of_this_occupation = models.DateField('从事本职业工作开始时间', null=True, blank=True)

    current_certificate_number = models.CharField('本次考核证书编号', max_length=20, null=True, blank=True,
                                                  help_text='本次考核证书编号')
    current_issue_unit = models.CharField("本次考核职业资格证书发行单位", max_length=100, default='', help_text='职业资格证书发行单位',
                                          blank=True, null=True,)
    current_issuance_time = models.DateField('本次考核职业资格证书发行时间', blank=True, null=True)
    declaration_of_occupation = models.CharField('申报职业', max_length=20, null=False, blank=False, help_text='申报职业')
    career_life = models.SmallIntegerField('本次申报职业年限', default=0, blank=True, null=True, help_text='本次申报职业年限')
    career_orientation = models.CharField('职业方向', max_length=50, null=True, blank=True, help_text='职业方向')
    identification_level = models.CharField('鉴定级别', max_length=50, blank=False, help_text='鉴定级别',
                                            default=99,
                                            choices=[('1', '高级技工'),
                                                     ('2', '技工'),
                                                     ('3', '高级'),
                                                     ('4', '中级'),
                                                     ('5', '初级'),
                                                     ('99', '无级别信息')])

    work_training = models.TextField('个人工作及职业培训简历', max_length=500, null=True, blank=True, help_text='个人工作及职业培训简历')

    condition_selected = models.CharField('申报条件代码', max_length=50, null=True, blank=True, help_text='申报条件代码')
    # working_record = models.ManyToManyField(WorkingHistory, through='WorkingHistoryStudentRLS',
    #                                         through_fields=('working_history', 'student_info'))

    school_name = models.CharField('毕业院校名称', max_length=50, null=True, blank=True, help_text='毕业院校名称')
    graduation_status = models.IntegerField(help_text="毕业证件状态", verbose_name='毕业证件状态', null=True, default=0)
    graduation_result = models.CharField('毕业结业状态', max_length=50, default=1,
                                         choices=[('1', '已毕业'),
                                                  ('2', '未毕业')],
                                         help_text='1-已毕业/2-未毕业')
    major = models.CharField(verbose_name='专业或相关专业', max_length=50, default="", help_text='专业或相关专业', null=True,
                             blank=True)
    course_hours = models.IntegerField(help_text='培训课时', null=True, default=0)
    graduation_time = models.DateField('毕业时间', null=True, blank=True)

    apprentice_start = models.DateField(help_text="学徒期开始", null=True, blank=True)
    apprentice_end = models.DateField(help_text="学徒期结束", null=True, blank=True)
    apprentice_year = models.IntegerField(help_text='学徒期年', null=True, default=0)
    apprentice_month = models.IntegerField(help_text='学徒期月', null=True, default=0)
    original_certificate_worker_year = models.IntegerField('从事本职业工作年限（后）', null=True, blank=True, default=0,
                                                           help_text='从事本职业工作年限（后），获取资格证之后')
    record_status = models.CharField('填报状态', max_length=50, default=1,
                                     choices=[('1', '启用'),
                                              ('2', '停用')],
                                     help_text='1-启用/2-停用')
    submit_status = models.CharField('提交状态', max_length=50, default=2,
                                     choices=[('1', '已提交'),
                                              ('2', '未提交')],
                                     help_text='1 提交 2 未 提交,一旦提交,学员将无法编辑修改,信息的操作权限将转移到上一级的负责人手中,默认是未提交')
    review_status = models.CharField('检查状态', max_length=50, default=2,
                                     choices=[('1', '已审核'),
                                              ('2', '未审核')],
                                     help_text='1 已审核2 未审核,一旦审核,负责人将无法编辑修改,信息的操作权限将转移到上一级的系统超级管理员手中')
    cancel_status = models.CharField('是否提交注销申请', max_length=50, default=2,
                                     choices=[('1', '申请撤销'),
                                              ('2', '未申请撤销')],
                                     help_text='1 申请撤销 2 未申请撤销,一旦申请被受理,学员将无法编辑修改,信息的操作权限将转移到上一级的负责人手中')
    cancel_result = models.CharField('提交撤销状态', max_length=50, default=2,
                                     choices=[('1', '申请撤销成功'),
                                              ('2', '申请撤销失败')],
                                     help_text='1 申请撤销成功 2 申请撤销失败,一旦负责人同意撤销,负责人将无法编辑修改,信息的操作权限将转移到下一级的学员手中')
    teacher_cancel_status = models.CharField('负责人提交注销申请', max_length=50, default=2,
                                             choices=[('1', '申请撤销'),
                                                      ('2', '未申请撤销')],
                                             help_text='1 申请撤销 2 未申请撤销,一旦申请被受理,负责人将无法编辑修改此纪录,信息的操作权限将转移到上一级的管理员手中')
    teacher_cancel_result = models.CharField('负责人申请注销状态', max_length=50, default=2,
                                             choices=[('1', '申请撤销成功'),
                                                      ('2', '申请撤销失败')],
                                             help_text='1 申请撤销成功 2 申请撤销失败,一旦管理员同意注销,将无法编辑修改,信息的操作权限将转移到对应的负责人手中')
    confirm_status = models.CharField('检查状态', max_length=50, default=2,
                                      choices=[('1', '已确认'),
                                               ('2', '未确认')],
                                      help_text='1 已确认 2 未确认,一旦超级管理员确认,填报信息将最终生效,并进入缴费确认状态，学员将无法提交注销申请！')
    # 后加缴费情况
    pay_status = models.CharField('支付状态', max_length=50, default=2,
                                  choices=[('1', '已支付'),
                                           ('2', '未支付')],
                                  help_text='1 已支付 2 未支付,一旦支付,学员信息将进入学习状态')

    chemical_worker = models.CharField('化工', max_length=50, default=2,
                                       choices=[('1', '化工'),
                                                ('2', '非化工')],
                                       help_text='1 化工 2 非化工')

    payment_amount = models.IntegerField('已缴费金额', help_text='已缴费金额', default=0, null=True)
    unpaid_amount = models.IntegerField('未缴费金额', help_text='未缴费金额', default=0, null=True)
    study_status = models.CharField('学业状态', max_length=50, default=2,
                                    choices=[('1', '正常'),
                                             ('2', '异常')],
                                    help_text='1 正常 2 异常,异常应在备注中说明')
    # 成绩管理
    examination_status = models.CharField('考核状态', max_length=50, default=2,
                                          choices=[('1', '已通过'),
                                                   ('2', '未通过')],
                                          help_text='1 已通过2 未通过,一旦通过,将结束这条信息的操作使命')
    # 考核成绩
    theoretical_achievements = models.SmallIntegerField('考核理论成绩', default=0, null=True, help_text='考核理论成绩', blank=True)
    practical_operation = models.SmallIntegerField('考核实际操作成绩', default=0, null=True, help_text='考核实际操作成绩', blank=True)
    # 后加考核部分
    
    # 新增属性20200518
    student_source_class = models.ForeignKey('StudentSourceClass', to_field='id',
                                    related_name="%(app_label)s_%(class)s_StudentSourceClass",
                                    verbose_name='学生来源',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='学生来源')
    identify_subject = models.ForeignKey('IdentifySubject', to_field='id',
                                    related_name="%(app_label)s_%(class)s_IdentifySubject",
                                    verbose_name='鉴定科目',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='鉴定科目')
    identify_class = models.ForeignKey('IdentifyClass', to_field='id',
                                    related_name="%(app_label)s_%(class)s_IdentifyClass",
                                    verbose_name='鉴定类别',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='鉴定类别')
    subside_class = models.ForeignKey('SubsideClass', to_field='id',
                                    related_name="%(app_label)s_%(class)s_SubsideClass",
                                    verbose_name='补贴类别',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='补贴类别')
    subside_certificate_class = models.ForeignKey('SubsideCertificateClass', to_field='id',
                                    related_name="%(app_label)s_%(class)s_SubsideCertificateClass",
                                    verbose_name='补贴证件类别',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='补贴证件类别')
    subside_certificate_number = models.CharField('补贴证书编号', max_length=20, default='', null=True, blank=True,
                                                   help_text='补贴证书编号')
    # examinee_type = models.ForeignKey('ExamineeType', to_field='id',
    #                                 related_name="%(app_label)s_%(class)s_ExamineeType",
    #                                 verbose_name='考生类别',
    #                                 blank=True,
    #                                 null=True,
    #                                 on_delete=models.CASCADE,
    #                                 help_text='考生类别')

    examinee_identity = models.ForeignKey('ExamineeIdentity', to_field='id',
                                    related_name="%(app_label)s_%(class)s_ExamineeType",
                                    verbose_name='考生身份',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='考生身份')

    place_sign_up = models.ForeignKey('PlaceSignUp', to_field='id',
                                    related_name="%(app_label)s_%(class)s_PlaceSignUp",
                                    verbose_name='预报名点',
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    help_text='预报名点')
    explain = models.TextField('说明', default='', max_length=200, null=True, blank=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '学生填报详细信息'
        verbose_name_plural = '学生填报详细信息'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)

# class WorkingHistoryStudentRLS(models.Model):
#     """
#     学生和工作年限证明关系表
#     """
#     id = models.AutoField('用户ID', primary_key=True)
#     working_history = models.ForeignKey(WorkingHistory,
#                                         on_delete=models.CASCADE,
#                                         related_name='WorkingHistory_StudentInfo',
#                                         null=False,
#                                         blank=False,
#                                         verbose_name='历史工作单位',
#                                         help_text='历史工作单位')
#     student_info = models.ForeignKey(StudentInfo,
#                                      on_delete=models.CASCADE,
#                                      related_name='StudentInfo_WorkingHistory',
#                                      null=False,
#                                      blank=False,
#                                      verbose_name='学生',
#                                      help_text='学生')
#
#     class Meta:
#         ordering = ['id']
#
#     def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
#         if print_all:
#             # return ' '.join(('%s' % item for item in self.__dict__.values()))
#             return str(self.__dict__)
#         else:
#             return str(self.id)


class InterviewAudit(models.Model):
    """ 操作审计 不需要修改，只是查看"""
    id = models.AutoField('审计记录ID', primary_key=True)
    username = models.CharField('用户名', default='', blank=True, max_length=50, help_text='操作本次记录的用户名')
    operation = models.CharField('操作请求', default='', blank=True, max_length=50, help_text='操作本次记录的请求信息')
    ip_address = models.GenericIPAddressField('IP地址', default='', max_length=50, help_text='操作本次记录的客户端IP地址')
    operation_level = models.CharField('学业状态', max_length=50, default=1,
                                       choices=[('1', '查询'),
                                                ('2', '增加'),
                                                ('3', '修改状态'),
                                                ('4', '修改内容'),
                                                ('5', '删除'),
                                                ('6', '注册'),
                                                ('7', '登陆'),
                                                ('8', '退出'),
                                                ('9', '下载'),
                                                ('10', '上传')],
                                       help_text='1 正常 2 异常,异常应在备注中说明')
    operation_content = models.TextField('操作内容', default='', blank=True)
    operation_result = models.CharField('操作结果', default='', max_length=50, blank=True)
    operation_message = models.TextField('日志信息', default='', blank=True)
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '操作审计(不需要修改，只是查看或者删除)'
        verbose_name_plural = '操作审计(不需要修改，只是查看或者删除)'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.ip_address


class SystemMessage(models.Model):
    """站内系统信息管理类"""
    id = models.AutoField('系统信息ID', primary_key=True)
    sender = models.ForeignKey(UserInfo,
                               to_field='id',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='RegisterUserInfo_Sender',
                               verbose_name='发送方',
                               help_text='发送方')
    receiver = models.ForeignKey(UserInfo,
                                 to_field='id',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='RegisterUserInfo_Receiver',
                                 verbose_name='接收方',
                                 help_text='接收方')
    message_range = models.CharField('消息发送范围', max_length=50, default='', null=True, help_text='消息发送范围',
                                     choices=[('1', '系统公告'),
                                              ('2', '系统管理员'),
                                              ('3', '全体负责人'),
                                              ('4', '负责人'),
                                              ('5', '全体学员'),
                                              ('6', '负责人管辖全体学员'),
                                              ('7', '学员'),
                                              ('8', '单位报名负责人')])
    message_level = models.CharField('消息级别', max_length=50, default=1, null=True, help_text='消息级别',
                                     choices=[('1', '常规'),
                                              ('2', '预警'),
                                              ('3', '紧急')])
    message_title = models.CharField('消息标题', default='', max_length=50, blank=False, null=False, help_text='消息标题不可为空！')
    message_content = models.TextField('消息内容', default='', max_length=500, null=True, help_text='消息内容')
    send_status = models.CharField('发送状态', max_length=50, default=1,
                                   choices=[('1', '成功'),
                                            ('2', '失败')],
                                   help_text='1 成功 2 失败,发送成功,将以系统消息的方式提示接收方')
    receive_status = models.CharField('查看状态', max_length=50, default=2,
                                      choices=[('1', '已查看'),
                                               ('2', '未查看')],
                                      help_text='1 已查看 2 未查看,查看之后将不再会被推送为系统消息')
    feedback_status = models.CharField('确认状态', max_length=50, default=2,
                                       choices=[('1', '已确认'),
                                                ('2', '未确认')],
                                       help_text='1 已确认表明本次通话的结束 2 未确认表明本次信息已查看但但未确认信息给回馈者')
    hidden_status_sender = models.CharField('发送人隐藏消息状态', max_length=50, default=2,
                                            choices=[('1', '已隐藏'),
                                                     ('2', '未隐藏')],
                                            help_text='1 已隐藏将不会显示在查看列表中 2 未隐藏将显示在查看列表中')
    hidden_status_receiver = models.CharField('发送人隐藏消息状态', max_length=50, default=2,
                                              choices=[('1', '已隐藏'),
                                                       ('2', '未隐藏')],
                                              help_text='1 已隐藏将不会显示在查看列表中 2 未隐藏将显示在查看列表中')

    reply_status = models.CharField('确认并回复状态', max_length=50, default=2,
                                    choices=[('1', '已确认并回复'),
                                             ('2', '未确认未回复')],
                                    help_text='1 已确认并回复 2 未确认未回复')

    feedback_message = models.ForeignKey('SystemMessage',
                                         to_field='id',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='RegisterUserInfo_Sender',
                                         verbose_name='确认并回复消息',
                                         help_text='确认并回复消息')
    explain = models.TextField('说明', default='', max_length=200, null=True, blank=True)
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    modify_time = models.DateTimeField('修改时间', auto_now=True)  # 使用Model.save()来更新才会更新注意
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '站内系统信息管理类'
        verbose_name_plural = '站内系统信息管理类'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return str(self.id)

class ReportSkillMainClass(models.Model):
    """
    报名工种大类
    """
    id = models.AutoField('技能大类ID', primary_key=True)
    skill_main_class_code = models.CharField('技能大类编号',default='empty',
                                  max_length=50,
                                #   unique=True,
                                #   null=False,
                                  help_text='技能大类编号')
    skill_main_class_name = models.CharField('技能大类名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='技能大类名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '报名工种大类表'
        verbose_name_plural = '报名工种大类表'
    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.skill_main_class_name
# from .models_report import ReportBase
class ReportSkill(models.Model):
    """
    报名工种
    """
    skill_id = models.AutoField('技能ID', primary_key=True)
    skill_main_class = models.ForeignKey('ReportSkillMainClass', to_field='id',
                                      related_name="%(app_label)s_%(class)s_技能工种大类ID",
                                      verbose_name='技能工种大类ID',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='技能工种大类ID')
    skill_main_class_name = models.ForeignKey('ReportSkillMainClass', to_field='skill_main_class_name',
                                      related_name="%(app_label)s_%(class)s_技能工种大类名称",
                                      verbose_name='技能工种大类名称',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='技能工种大类名称')
    skill_code = models.CharField('技能编号',default='empty',
                                  max_length=50,
                                #   unique=True,
                                #   null=False,
                                  help_text='技能编号')
    skill_name = models.CharField('技能名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='技能名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['skill_id']
        verbose_name = '报名工种表'
        verbose_name_plural = '报名工种表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.skill_name


class ReportCondition(models.Model):
    """
    报名条件
    """
    condition_id = models.AutoField('条件ID', primary_key=True)
    condition_name = models.CharField('条件名称',
                                      max_length=50,
                                      unique=True,
                                      null=False,
                                      help_text='技能名称')
    condition_level = models.CharField('条件等级', max_length=50, default=1, null=True, help_text='条件等级',
                                       choices=[('5', '初级(五级)'),
                                                ('4', '中级(四级)'),
                                                ('3', '高级(三级)')])
    record_status = models.CharField('状态', max_length=50, default=2,
                                    choices=[('1', '启用'),
                                            ('2', '停用')],
                                    help_text='1-启用/2-停用')
    # 技能条件
    condition_for_skill = models.ForeignKey(ReportSkill, to_field='skill_id',
                                            on_delete=models.SET_NULL,
                                            related_name='Diploma_Condition_skill_所属技能ID',
                                            null=True,
                                            verbose_name='所属技能ID',
                                            help_text='所属技能ID')
    
    condition_for_skill_name = models.ForeignKey(ReportSkill, to_field='skill_name',
                                            on_delete=models.SET_NULL,
                                            related_name='Diploma_Condition_skill_name_所属技能名称',
                                            null=True,
                                            verbose_name='所属技能名称',
                                            help_text='所属技能名称')
    
    apprentice_status = models.CharField('学徒信息', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                            ('2', '不填写')],
                                    help_text='1-填写/2-填写')
    work_of_this_occupation_status = models.CharField('从事本工作时间', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不停用')],
                                    help_text='1-填写/2-填写')
    
    work_of_this_occupation_requirement = models.SmallIntegerField('从事本工作时间要求', default=0, null=True, help_text='获得现有资格证书后工作年限要求', blank=True)

    primary_level_status = models.CharField('填写原证书级别', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不填写')],
                                    help_text='1-填写/2-不填写')
    
    primary_level_requirement = models.CharField('原证书级别', max_length=50, default=0,
                                    choices=[('0', '不填写'),
                                             ('5', '初级(五级)'),
                                             ('4', '中级(四级)'),
                                             ('3', '高级(三级)')],
                                    help_text='1-**/0-不填写')
    original_certificate_info_status = models.CharField('原证书详细信息', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不填写')],
                                    help_text='1-填写/2-不填写')
    
    original_certificate_worker_time_status = models.CharField('获得现有资格证书后工作年限', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不填写')],
                                    help_text='1-填写/2-不填写')
    
    original_certificate_worker_time_requirement = models.SmallIntegerField('获得现有资格证书后工作年限要求', default=0, null=True, help_text='获得现有资格证书后工作年限要求', blank=True)
    school_info_status = models.CharField('学校及专业信息', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不填写')],
                                    help_text='1-填写/2-不填写')
    
    graduation_time_status = models.CharField('毕业(结业)信息', max_length=50, default=2,
                                    choices=[('1', '填写'),
                                             ('2', '不填写')],
                                    help_text='1-填写/2-不填写')
    graduation_low_requirement = models.CharField('学历要求或最低学历要求', max_length=50, default=1,
                                    choices=[('1', '-初级中学-'),
                                             ('2', '-技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('3', '-中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('4', '-高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('5', '-高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('6', '-大专及以上本专业或相关专业毕业证书-'),
                                             ('7', '-大学本科本专业或相关专业毕业证书-'),
                                             ('8', '-硕士研究生及以上本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('9', '-本职业初级正规培训-'),
                                             ('10', '-本职业中级正规培训结业证书-'),
                                             ('11', '-本职业高级正规培训结业证书-')],
                                    help_text='1-填写/2-不填写')
    
    graduation_lowest = models.CharField('是否是最低学历', max_length=50, default=2,
                                    choices=[('1', '是'),
                                             ('2', '不是')],
                                    help_text='1-填写/2-不填写')
    graduation_is_Fresh = models.CharField('是否在校应届生', max_length=50, default=2,
                                    choices=[('1', '是'),
                                             ('2', '不是')],
                                    help_text='1-是/2-不是')
    graduation_extra_two = models.CharField('学历要求(2)', max_length=50, default=0,
                                    choices=[('0', '-不填写-'),
                                             ('1', '-初级中学-'),
                                             ('2', '-技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('3', '-中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('4', '-高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('5', '-高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('6', '-大专及以上本专业或相关专业毕业证书-'),
                                             ('7', '-大学本科本专业或相关专业毕业证书-'),
                                             ('8', '-硕士研究生及以上本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('9', '-本职业初级正规培训-'),
                                             ('10', '-本职业中级正规培训结业证书-'),
                                             ('11', '-本职业高级正规培训结业证书-')],
                                    help_text='1-填写/2-不填写')
    graduation_extra_three = models.CharField('学历要求(3)', max_length=50, default=0,
                                    choices=[('0', '-不填写-'),
                                             ('1', '-初级中学-'),
                                             ('2', '-技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('3', '-中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('4', '-高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('5', '-高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('6', '-大专及以上本专业或相关专业毕业证书-'),
                                             ('7', '-大学本科本专业或相关专业毕业证书-'),
                                             ('8', '-硕士研究生及以上本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-'),
                                             ('9', '-本职业初级正规培训-'),
                                             ('10', '-本职业中级正规培训结业证书-'),
                                             ('11', '-本职业高级正规培训结业证书-')],
                                    help_text='1-填写/2-不填写')
    
    certificate_photos_status = models.CharField('资格证件照片', max_length=50, default=2,
                                    choices=[('1', '上传'),
                                             ('2', '不上传')],
                                    help_text='1-上传/2-不上传')

    diploma_certificate_photos_status = models.CharField('毕业证件照片', max_length=50, default=2,
                                    choices=[('1', '上传'),
                                             ('2', '不上传')],
                                    help_text='1-上传/2-不上传')
    
    explain_condition = models.TextField('备注（条件项说明）',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['condition_id']
        verbose_name = '报名条件设置表'
        verbose_name_plural = '报名条件设置表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.condition_name


class LevelCodeClass(models.Model):
    """
    级别编码表
    """
    id = models.AutoField('自动编码ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '级别编码表'
        verbose_name_plural = '级别编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        
class SexClass(models.Model):
    """
    性别编码表
    """
    id = models.AutoField('自动编码ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '性别编码表'
        verbose_name_plural = '性别编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        
        
class StudentSourceClass(models.Model):
    """
    考生来源编码表
    """
    id = models.AutoField('考生来源编码ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '考生来源编码表'
        verbose_name_plural = '考生来源编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        
class IdentifySubject(models.Model):
    """
    鉴定科目编码表
    """
    id = models.AutoField('考生来源编码ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '鉴定科目编码表'
        verbose_name_plural = '鉴定科目编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        

class IdentifyClass(models.Model):
    """
    鉴定类别编码表
    """
    id = models.AutoField('鉴定类别ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '鉴定类别编码表'
        verbose_name_plural = '鉴定类别编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        
class SubsideClass(models.Model):
    """
    补贴类别编码表
    """
    id = models.AutoField('补贴类别ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '补贴类别编码表'
        verbose_name_plural = '补贴类别编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        
class SubsideCertificateClass(models.Model):
    """
    补贴证件类别编码表
    """
    id = models.AutoField('补贴证件类别ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '补贴证件类别编码表'
        verbose_name_plural = '补贴证件类别编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name
        

# class ExamineeType(models.Model):
#     """
#     考生类别编码表
#     """
#     id = models.AutoField('考生类别ID', primary_key=True)
#     code = models.CharField('手动ID',default='empty',
#                                   max_length=50,
#                                   unique=True,
#                                   null=False,
#                                   help_text='手动ID')
#     name = models.CharField('名称',
#                                   max_length=50,
#                                   unique=True,
#                                   null=False,
#                                   help_text='名称')
#     record_status = models.CharField('状态', max_length=50, default=1,
#                                   choices=[('1', '启用'),
#                                            ('2', '停用')],
#                                   help_text='1-启用/2-停用')
#     explain = models.TextField('说明',
#                                default='',
#                                max_length=200,
#                                blank=True,
#                                null=True)
#     user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
#                                       related_name="%(app_label)s_%(class)s_操作用户",
#                                       verbose_name='操作用户',
#                                       blank=True,
#                                       null=True,
#                                       on_delete=models.SET_NULL,
#                                       help_text='操作用户记录')
#     create_time = models.DateTimeField('生成时间', default=timezone.now)
#     # 使用Model.save()来更新才会更新注意
#     modify_time = models.DateTimeField('修改时间', auto_now=True)
#     objects = models.Manager()

#     class Meta:
#         ordering = ['id']
#         verbose_name = '考生类别编码表'
#         verbose_name_plural = '考生类别编码表'

#     def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
#         if print_all:
#             # return ' '.join(('%s' % item for item in self.__dict__.values()))
#             return str(self.__dict__)
#         else:
#             return self.name

class ExamineeIdentity(models.Model):
    """
    考生身份编码表
    """
    id = models.AutoField('考生身份ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '考生身份编码表'
        verbose_name_plural = '考生身份编码表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name

class PlaceSignUp(models.Model):
    """
    预报名地点表
    """
    id = models.AutoField('ID', primary_key=True)
    code = models.CharField('手动ID',default='empty',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='手动ID')
    name = models.CharField('名称',
                                  max_length=50,
                                  unique=True,
                                  null=False,
                                  help_text='名称')
    record_status = models.CharField('状态', max_length=50, default=1,
                                  choices=[('1', '启用'),
                                           ('2', '停用')],
                                  help_text='1-启用/2-停用')
    explain = models.TextField('说明',
                               default='',
                               max_length=200,
                               blank=True,
                               null=True)
    user_operator = models.ForeignKey('RegisterUserInfo', to_field='id',
                                      related_name="%(app_label)s_%(class)s_操作用户",
                                      verbose_name='操作用户',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      help_text='操作用户记录')
    create_time = models.DateTimeField('生成时间', default=timezone.now)
    # 使用Model.save()来更新才会更新注意
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = '预报名地点表'
        verbose_name_plural = '预报名地点表'

    def __str__(self, print_all=False):  # 定义打印对象时打印的字符串
        if print_all:
            # return ' '.join(('%s' % item for item in self.__dict__.values()))
            return str(self.__dict__)
        else:
            return self.name