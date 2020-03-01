from webapp.controller import role, report, teacher, administrator, download, student, user, website, system_message, \
    love as love_m
from webapp.controller.search import administrator as administrator_search, user as user_search, \
    teacher as teacher_search


def introduction(request):
    """
    进入报考简介页面
    :param request:
    :return:
    """
    return website.introduction(request)


def system_guide(request):
    """
    进入报考简介页面
    :param request:
    :return:
    """
    return website.system_guide(request)


def role_info(request):
    """
    角色管理
    :param request:
    :return:
    """
    return role.role_info_list(request)


def index(request):
    """
    网站首页
    :param request:
    :return:
    """
    return website.index(request)


def to_login(request):
    """
    返回登陆页面
    :param request:
    :return:
    """
    return website.to_login(request)


def sign_out(request):
    """
    推出网站
    :param request:
    :return:
    """
    return website.sign_out(request)


def check_username(request):
    """
    检查用户名使用情况
    :param request:
    :return:
    """
    return website.check_username(request)


def check_nickname(request):
    """
    检测昵称使用情况
    :param request:
    :return:
    """
    return website.check_nickname(request)


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return website.register(request)


def sign_in(request):
    """
    登陆网站
    :param request:
    :return:
    """
    return website.sign_in(request)


def to_index(request):
    """
    返回网站首页
    :param request:
    :return:
    """
    return website.to_index(request)


def to_index_teacher(request):
    """
    负责人首页
    :param request:
    :return:
    """
    return website.to_index_teacher(request)


def report_info_review(request):
    """
    负责人审核学生信息
    :return:
    """
    return teacher.report_info_review(request)


def report_do_review(request):
    """
    负责人开始审核学生信息
    :return:
    """
    return teacher.report_do_review(request)


def report_do_review_cancel(request):
    """
        负责人取消审核学生信息
        :return:
        """
    return teacher.report_do_review_cancel(request)


def report_do_confirm(request):
    """
    系统管理员进行学员信息的最终确认
    :return:
    """
    return administrator.report_do_confirm(request)


def report_cancel_confirm(request):
    """
    系统管理员取消信息确认
    :param request:
    :return:
    """
    return administrator.report_cancel_confirm(request)


def admin_del_student(request):
    """
    系统管理员删除学生信息
    :param request:
    :return:
    """
    return administrator.admin_del_student(request)


def administrator_all_student_base_info(request):
    """
    学员报名表
    :param request:
    :return:
    """
    return administrator.administrator_all_student_base_info(request)


def administrator_reporter_chemical_not(request):
    """
    学员报名表
    :param request:
    :return:
    """
    return administrator.administrator_reporter_chemical_not(request)


def administrator_reporter_chemical(request):
    """
    学员报名表
    :param request:
    :return:
    """
    return administrator.administrator_reporter_chemical(request)


def administrator_search_chemical(request):
    """
    附带条件查询化工类学生花名册
    :param request:
    :return:
    """
    return administrator_search.administrator_search_chemical(request)


def administrator_search_wait_confirm(request):
    """
    附带条件查询化工类学生花名册
    :param request:
    :return:
    """
    return administrator_search.administrator_search_wait_confirm(request)


def administrator_search_chemical_download(request):
    """
    带条件查询，然后下载对应结果文件
    :param request:
    :return:
    """
    return download.administrator_search_chemical_download(request)


def administrator_search_chemical_not_download(request):
    """
    带条件查询，然后下载对应结果文件
    :param request:
    :return:
    """
    return download.administrator_search_chemical_not_download(request)


def all_student_base_info_download(request):
    """
    带条件查询，然后下载对应结果文件
    :param request:
    :return:
    """
    return download.all_student_base_info_download(request)


def administrator_search_chemical_not(request):
    """
    附带条件查询非化工类学生花名册
    :param request:
    :return:
    """
    return administrator_search.administrator_search_chemical_not(request)


def administrator_search_all_student(request):
    """
    附带条件查询非化工类学生花名册
    :param request:
    :return:
    """
    return administrator_search.administrator_search_all_student(request)


def report_info_confirm(request):
    """
    确认填报的信息
    :return:
    """
    return administrator.report_info_confirm(request)


def admin_term_picture_data(request):
    """
    批量下载证件
    :param request:
    :return:
    """
    return administrator.admin_term_picture_data(request)


def del_register_info(request):
    """
    批量下载证件
    :param request:
    :return:
    """
    return administrator.del_register_info(request)


def report_teacher_list(request):
    """
    负责人列表
    :return:
    """
    return administrator.report_teacher_list(request)


def report_operation_log_list(request):
    """
    返回常规操作的日志列表
    :param request:
    :return:
    """
    return administrator.report_operation_log_list(request)


def report_system_info_detail(request):
    """
    获取服务器运行时主要数据
    :param request:
    :return:
    """
    return administrator.report_system_info_detail(request)


def report_delete_force(request):
    """
    深度删除
    :param request:
    :return:
    """
    return administrator.report_delete_force(request)


def delete_force(request):
    """
    深度清理
    :param request:
    :return:
    """
    return administrator.delete_force(request)


def to_update_teacher(request):
    """
    携带数据返回更新页面
    :return:
    """
    return teacher.to_update_teacher(request)


def update_teacher_info(request):
    """
    更新单位负责人的信息
    :param request:
    :return:
    """
    return teacher.update_teacher_info(request)


def cancel_teacher(request):
    """
    删除负责人信息
    :param request:
    :return:
    """
    return teacher.cancel_teacher(request)


def start_teacher(request):
    """
    删除负责人信息
    :param request:
    :return:
    """
    return teacher.start_teacher(request)


def report_school_term_list(request):
    """
    报名时间设置
    :return:
    """
    return administrator.report_school_term_list(request)


def add_school_term(request):
    """
    添加新一期报名开始、截止时间
    :param request:
    :return:
    """
    return administrator.add_school_term(request)


def update_school_term(request):
    """
    添加新一期报名开始、截止时间
    :param request:
    :return:
    """
    return administrator.update_school_term(request)


def del_term_info(request):
    """
    删除本报名周期的设置
    :param request:
    :return:
    """
    return administrator.del_term_info(request)


def admin_del_term_info_data(request):
    """
    管理员删除当前学期的填报数据
    :param request:
    :return:
    """
    return administrator.admin_del_term_info_data(request)


def refresh_school_term_data(request):
    """
    刷新统计本期报名数据
    :param request:
    :return:
    """
    return administrator.refresh_school_term_data(request)


def to_update_term_info(request):
    """
    带数据转到修改的弹框页面
    :return:
    """
    return administrator.to_update_term_info(request)


def register_teacher(request):
    """
    通过注册的方式添加负责人
    :param request:
    :return:
    """
    return administrator.register_teacher(request)


# start business

def worker(request):
    """
    根据工种分配填报页面
    :param request:
    :return:
    """
    return report.worker(request)


def education_degree(request):
    """
    获取教育程度信息
    :param request:
    :return:
    """
    return report.education_degree(request)


def unit_nature(request):
    """
    获取单位性质信息
    :param request:
    :return:
    """
    return report.unit_nature(request)


def nation_info(request):
    """
    获取民族信息
    :param request:
    :return:
    """
    return report.nation_info(request)


def teacher_info(request):
    """
    获取民族信息
    :param request:
    :return:
    """
    return report.teacher_info(request)


def add_student_info(request):
    """
    保存学生的信息
    :param request:
    :return:
    """
    return student.add_student_info(request)


def report_student_info_list(request):
    """
    学生填报基本信息列表
    :param request:
    :return:
    """
    return student.report_student_info_list(request)


def report_student_payment(request):
    """
    学员进行缴费
    :param request:
    :return:
    """
    return student.report_student_payment(request)


def student_info_detail(request):
    """
    详情查看
    :return:
    """
    return student.student_info_detail(request)


def to_student_info_update(request):
    """
    修改学生填报信息
    :return:
    """
    return student.to_student_info_update(request)


def student_info_update(request):
    """
    修改学生填报信息
    :return:
    """
    return student.student_info_update(request)


def report_student_del(request):
    """
    删除未提交的报名信息
    :param request:
    :return:
    """
    return student.report_student_del(request)


def report_student_submit(request):
    """
    提交最终报名信息
    :param request:
    :return:
    """
    return student.report_student_submit(request)


def report_student_cancel(request):
    """
    申请注销最终报名信息
    :param request:
    :return:
    """
    return student.report_student_cancel(request)


def report_student_cancel_return(request):
    """
    撤销注销最终报名信息
    :param request:
    :return:
    """
    return student.report_student_cancel_return(request)


# ====================================================================================


def province(request):
    """
    保存学生的信息
    :param request:
    :return:
    """
    return report.province(request)


def city(request):
    """
    保存学生的信息
    :param request:
    :return:
    """
    return report.city(request)


def county(request):
    """
    保存学生的信息
    :param request:
    :return:
    """
    return report.county(request)


def image_upload(request):
    """
    图片上传
    :param request:
    :return:
    """
    return report.image_upload(request)


def worker_history(request):
    """
    跳转到工作经验证明的页面
    :param request:
    :return:
    """
    return report.worker_history(request)


def add_work_history(request):
    """
    添加工作经验历史
    :param request:
    :return:
    """
    return report.add_work_history(request)


def delete_history(request):
    """
    删除工作经验
    :param request:
    :return:
    """
    return report.delete_history(request)


def download_apply(request):
    """
    生成对应的申请表文件
    :param request:
    :return:
    """
    return download.download_apply(request)


def start_download(request):
    """
    开始下载文件
    :param request:
    :return:
    """
    return download.start_download(request)


def all_student_base_info(request):
    """
    生成对应的所有确认过的学生信息
    :return:
    """
    return download.all_student_base_info(request)


def reporter_chemical_not(request):
    """
    生成所有非化学类的学生花名册
    :return:
    """
    return download.reporter_chemical_not(request)


def reporter_chemical(request):
    """
    生成所有非化学类的学生花名册
    :return:
    """
    return download.reporter_chemical(request)


def report_download_page(request):
    """
    跳转至最新网页
    :param request:
    :return:
    """
    return download.report_download_page(request)


def add_user_info(request):
    """
    添加用户信息
    :param request:
    :return:
    """
    return user.add_user_info(request)


def update_user_info(request):
    """
    修改用户的基础信息
    :return:
    """
    return user.update_user_info(request)


def update_user_base_info(request):
    """
    修改用户基本信息
    :param request:
    :return:
    """
    return user.update_user_base_info(request)


def user_info_list(request):
    """
    附带注册信息，返回所有用户信息
    :param request:
    :return:
    """
    return user.user_info_list(request)


def user_setting(request):
    """
    查看用户基本信息
    :param request:
    :return:
    """
    return user.user_setting(request)


def to_user_info_update(request):
    """
    修改用户基本信息
    :param request:
    :return:
    """
    return user.to_user_info_update(request)


def reset_password(request):
    """
    请求修改密码
    :param request:
    :return:
    """
    return user.reset_password(request)


def reset_password_page(request):
    """
    跳转至重置密码页面
    :param request:
    :return:
    """
    return user.reset_password_page(request)


def check_origin_password(request):
    """
    检测原始密码是否正确
    :param request:
    :return:
    """
    return user.check_origin_password(request)


def final_reset_password(request):
    """
    最终修改账户名密码
    :param request:
    :return:
    """
    return user.final_reset_password(request)


def save_system_message(request):
    """
    保存并发送一个消息
    :param request:
    :return:
    """
    return system_message.save_system_message(request)


# system_message
def send(request):
    """
    发送信息列表
    :param request:
    :return:
    """
    return system_message.send(request)


def receive(request):
    """
    接收信息列表
    :param request:
    :return:
    """
    return system_message.receive(request)


def admin_message(request):
    """
    系统公告信息
    :param request:
    :return:
    """
    return system_message.admin_message(request)


def message_add(request):
    """
    添加一条信息
    :param request:
    :return:
    """
    return system_message.message_add(request)


def message_to_receiver(request):
    """
    添加一条信息
    :param request:
    :return:
    """
    return system_message.message_to_receiver(request)


def message_to_message(request):
    """
    添加一条信息
    :param request:
    :return:
    """
    return system_message.message_to_message(request)


def system_message_detail(request):
    """
    返回消息详情页面
    :param request:
    :return:
    """
    return system_message.system_message_detail(request)


def system_message_confirm(request):
    """
    确认查看信息
    :param request:
    :return:
    """
    return system_message.system_message_confirm(request)


def system_message_confirm_send(request):
    """
    确认查看信息
    :param request:
    :return:
    """
    return system_message.system_message_confirm_send(request)


def reply_system_message(request):
    """
    确认并回复消息
    :param request:
    :return:
    """
    return system_message.reply_system_message(request)


def system_message_hidden(request):
    """
    清理信息（隐藏信息）不再像用户展示，留存系统
    :param request:
    :return:
    """
    return system_message.system_message_hidden(request)


def get_like_user_info(request):
    """
    获取模糊查询的匹配结果
    :param request:
    :return:
    """
    return user_search.get_like_user_info(request)


# ===========================================================================
# teacher search

def teacher_search_wait_review(request):
    """
    负责人按条件查询属下学员
    :param request:
    :return:
    """
    return teacher_search.teacher_search_wait_review(request)


def love(request):
    return love_m.love(request)
