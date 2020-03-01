from django import forms


class UserInfoForm(forms.Form):
    student_id = forms.IntegerField()

    real_name = forms.CharField(max_length=50, )
    sex = forms.CharField(max_length=50)
    age = forms.IntegerField(help_text='年龄', required=False)
    email = forms.EmailField(max_length=50, required=False)
    # phone = forms.CharField(max_length=50, help_text='手机')
    birthday = forms.DateField(help_text="出生日期", required=False)

    id_number = forms.CharField(max_length=20, help_text='身份证件号码信息')
    work_unit = forms.CharField(max_length=100, help_text='工作单位信息,可为空！', required=False)

    contact_number = forms.CharField(max_length=50, help_text='联系电话')
    start_working_date = forms.DateField(help_text="起始工作时间", required=False)
    working_year = forms.IntegerField(help_text='小于10个月，默认为小数年。如果大于10个月约等于1年，参加工作年限', required=False)
    address = forms.CharField(max_length=200, help_text='常住住址')
    id_card_address = forms.CharField(max_length=200, help_text='身份证住址')
    postal_code = forms.CharField(max_length=20, help_text='邮政编码', required=False)
    political_status = forms.CharField(max_length=20)

    # 外键信息
    two_inch_photo_form = forms.IntegerField(required=False)
    # 后加的
    person_in_charge = forms.CharField(max_length=20, help_text='单位报名负责人')
    nation_info_form = forms.IntegerField(help_text="民族信息", required=False)
    fixed_telephone = forms.CharField(max_length=20, help_text='固定电话，带区号', required=False)
    unit_address = forms.CharField(max_length=200, help_text='工作单位地址', required=False)

    unit_nature_form = forms.IntegerField(help_text='单位性质', required=False)
    hukou_province_form = forms.IntegerField(required=False)
    hukou_city_form = forms.IntegerField(required=False)
    hukou_county_form = forms.IntegerField(required=False)
    education_degree_form = forms.IntegerField(help_text='文化程度', required=False)
    middle_school = forms.CharField(max_length=50, help_text='初级中学', required=False)
    main_occupation = forms.CharField(max_length=50, help_text='从事职业', required=False)
    teacher_info_form = forms.IntegerField(help_text='单位报名的负责人信息', required=False)
    # former_occupation = forms.CharField(max_length=20, help_text='原职业', required=False)

