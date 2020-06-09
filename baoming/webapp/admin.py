from django.contrib import admin
from .models import *

admin.site.site_title = "报名平台"
admin.site.site_header = "山东省德州市乐陵县杏林学校-后台管理系统"
# admin.site. = "山东省德州市乐陵县杏林学校"
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)


# 省县乡
class ProvinceCityCountryAdmin(admin.ModelAdmin):
    obj = ProvinceCityCountry()
    list_display = tuple(obj.__dir__()[1:9])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('region_name',)
    search_fields = ('id', 'region_name', 'region_level', 'region_status')


admin.site.register(ProvinceCityCountry, ProvinceCityCountryAdmin)


# 学历
class EducationDegreeAdmin(admin.ModelAdmin):
    obj = EducationDegree()
    list_display = tuple(obj.__dir__()[1:6])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('education_name',)
    search_fields = ('id', 'education_name')


admin.site.register(EducationDegree, EducationDegreeAdmin)


# 单位性质
class UnitNatureAdmin(admin.ModelAdmin):
    obj = UnitNature()
    list_display = tuple(obj.__dir__()[1:6])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('unit_nature',)
    search_fields = ('id', 'unit_nature')


admin.site.register(UnitNature, UnitNatureAdmin)


# 图片
class PictureAdmin(admin.ModelAdmin):
    obj = Picture()
    list_display = tuple(obj.__dir__()[1:9])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('picture_name',)
    search_fields = ('id', 'picture_name')


admin.site.register(Picture, PictureAdmin)

# 图片
class IDCardPictureAdmin(admin.ModelAdmin):
    obj = IDCardPicture()
    list_display = tuple(obj.__dir__()[1:9])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('picture_name',)
    search_fields = ('id', 'picture_name')


admin.site.register(IDCardPicture, IDCardPictureAdmin)


# 图片
class FileManageAdmin(admin.ModelAdmin):
    obj = FileManage()
    list_display = tuple(obj.__dir__()[1:9])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('file_name',)
    search_fields = ('id', 'file_name')


admin.site.register(FileManage, FileManageAdmin)


# 工作年限承诺书
class WorkingHistoryAdmin(admin.ModelAdmin):
    obj = WorkingHistory()
    list_display = tuple(obj.__dir__()[1:11])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('unit_name',)
    search_fields = ('id', 'unit_name')


admin.site.register(WorkingHistory, WorkingHistoryAdmin)


# 注册用户基本信息
class RegisterUserInfoAdmin(admin.ModelAdmin):
    obj = RegisterUserInfo()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id', 'username',)
    search_fields = ('id', 'username', 'nickname')


admin.site.register(RegisterUserInfo, RegisterUserInfoAdmin)


# 注册用户基本信息
class NationInfoAdmin(admin.ModelAdmin):
    obj = NationInfo()
    list_display = tuple(obj.__dir__()[1:6])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id', 'nation_name',)
    search_fields = ('id', 'nation_name')


admin.site.register(NationInfo, NationInfoAdmin)


# 用户基本信息
class UserInfoAdmin(admin.ModelAdmin):
    obj = UserInfo()
    list_display = tuple(obj.__dir__()[1:35])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id', 'real_name',)
    search_fields = ('id', 'real_name', 'work_unit')


admin.site.register(UserInfo, UserInfoAdmin)

# 用户基本信息
class TeacherInfoAdmin(admin.ModelAdmin):
    obj = TeacherInfo()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id', 'number',)
    search_fields = ('id', 'number',)


admin.site.register(TeacherInfo, TeacherInfoAdmin)

# 学生信息
class StudentInfoAdmin(admin.ModelAdmin):
    obj = StudentInfo()
    list_display = tuple(obj.__dir__()[1:63])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id',)
    search_fields = (
        'id', 'user_info', 'status', 'former_occupation', 'declaration_of_occupation', 'career_orientation')


admin.site.register(StudentInfo, StudentInfoAdmin)


class RoleInfoAdmin(admin.ModelAdmin):
    obj = RoleInfo()
    list_display = tuple(obj.__dir__()[1:7])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('role_name',)
    search_fields = ('id', 'role_name')


admin.site.register(RoleInfo, RoleInfoAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    obj = UserRole()
    list_display = tuple(obj.__dir__()[1:7])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id',)
    search_fields = ('id', 'user',)


admin.site.register(UserRole, UserRoleAdmin)


class RoleAuthorityAdmin(admin.ModelAdmin):
    obj = RoleAuthority()
    list_display = tuple(obj.__dir__()[1:7])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id',)
    search_fields = ('id', 'role')


admin.site.register(RoleAuthority, RoleAuthorityAdmin)


class UserAuthorityAdmin(admin.ModelAdmin):
    obj = UserAuthority()
    list_display = tuple(obj.__dir__()[1:7])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id',)
    search_fields = ('id', 'user',)


admin.site.register(UserAuthority, UserAuthorityAdmin)


class AuthorityMenuAdmin(admin.ModelAdmin):
    obj = AuthorityMenu()
    list_display = tuple(obj.__dir__()[1:7])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('authority_name',)
    search_fields = ('id', 'authority_name',)


admin.site.register(AuthorityMenu, AuthorityMenuAdmin)


class InterviewAuditAdmin(admin.ModelAdmin):
    obj = InterviewAudit()
    list_display = tuple(obj.__dir__()[1:10])
    readonly_fields = ('create_time',)
    list_display_links = ('id',)
    search_fields = ('id', 'operator', 'ip_address',)


admin.site.register(InterviewAudit, InterviewAuditAdmin)


class SystemMessageAdmin(admin.ModelAdmin):
    obj = SystemMessage()
    list_display = tuple(obj.__dir__()[1:13])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ('id',)
    search_fields = ('id', 'message', 'send_status', 'receive_status', 'feedback_status',)


admin.site.register(SystemMessage, SystemMessageAdmin)

class ReportSkillMainClassAdmin(admin.ModelAdmin):
    obj = ReportSkillMainClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'skill_main_class_name',)


admin.site.register(ReportSkillMainClass, ReportSkillMainClassAdmin)

class ReportSkillAdmin(admin.ModelAdmin):
    obj = ReportSkill()
    list_display = tuple(obj.__dir__()[1:10])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('skill_id', 'skill_name',)


admin.site.register(ReportSkill, ReportSkillAdmin)


class ReportConditionAdmin(admin.ModelAdmin):
    obj = ReportCondition()
    list_display = tuple(obj.__dir__()[1:30])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('condition_id', 'condition_name',)


admin.site.register(ReportCondition, ReportConditionAdmin)


class LevelCodeClassAdmin(admin.ModelAdmin):
    obj = LevelCodeClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(LevelCodeClass, LevelCodeClassAdmin)

class SexClassAdmin(admin.ModelAdmin):
    obj = SexClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(SexClass, SexClassAdmin)

class StudentSourceClassAdmin(admin.ModelAdmin):
    obj = StudentSourceClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(StudentSourceClass, StudentSourceClassAdmin)

class IdentifySubjectAdmin(admin.ModelAdmin):
    obj = IdentifySubject()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(IdentifySubject, IdentifySubjectAdmin)

class IdentifyClassAdmin(admin.ModelAdmin):
    obj = IdentifyClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(IdentifyClass, IdentifyClassAdmin)

class SubsideClassAdmin(admin.ModelAdmin):
    obj = SubsideClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(SubsideClass, SubsideClassAdmin)

class SubsideCertificateClassAdmin(admin.ModelAdmin):
    obj = SubsideCertificateClass()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(SubsideCertificateClass, SubsideCertificateClassAdmin)

# class ExamineeTypeAdmin(admin.ModelAdmin):
#     obj = ExamineeType()
#     list_display = tuple(obj.__dir__()[1:8])
#     readonly_fields = ('create_time', 'modify_time',)
#     list_display_links = ()
#     search_fields = ('id', 'name',)


# admin.site.register(ExamineeType, ExamineeTypeAdmin)


class ExamineeIdentityAdmin(admin.ModelAdmin):
    obj = ExamineeIdentity()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(ExamineeIdentity, ExamineeIdentityAdmin)


class PlaceSignUpAdmin(admin.ModelAdmin):
    obj = PlaceSignUp()
    list_display = tuple(obj.__dir__()[1:8])
    readonly_fields = ('create_time', 'modify_time',)
    list_display_links = ()
    search_fields = ('id', 'name',)


admin.site.register(PlaceSignUp, PlaceSignUpAdmin)
