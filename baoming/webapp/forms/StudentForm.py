from django import forms


class StudentForm(forms.Form):
    # 添加学生信息
    declaration_of_occupation = forms.CharField(max_length=20, help_text='申报职业')
    identification_level = forms.CharField(max_length=50, help_text='申报鉴定级别')

    condition_selected = forms.CharField(max_length=50, help_text='申报资质条件代码')

    apprentice_start = forms.DateField(help_text="学徒期开始", required=False)
    apprentice_end = forms.DateField(help_text="学徒期结束", required=False)
    apprentice_year = forms.IntegerField(help_text='学徒期年', required=False)
    apprentice_month = forms.IntegerField(help_text='学徒期月', required=False)

    profession = forms.CharField(max_length=50, help_text='从事职业', required=False)
    start_the_work_of_this_occupation = forms.DateField(help_text="从事本职业工作开始时间", required=False)
    career_life = forms.IntegerField(help_text='从事本职业工作年限，五资格证要求', required=False)

    # former_occupation = forms.CharField(max_length=20, help_text='原职业', required=False)

    original_certificate_worker_year = forms.IntegerField(help_text='从事本职业工作年限，获取资格证之后', required=False)

    original_certificate_number = forms.CharField(max_length=20, help_text='原证书编号', required=False)

    career_orientation = forms.CharField(max_length=50, help_text='职业方向', required=False)
    # status = forms.CharField(max_length=50, help_text='1-启用/2-停用')
    work_training = forms.CharField(max_length=500, help_text='个人工作及职业培训简历', required=False)

    issue_unit = forms.CharField(max_length=200, help_text='发证单位', required=False)
    issuance_time = forms.DateField(help_text='发行时间', required=False)

    graduation_status = forms.IntegerField(help_text="毕业状态", required=False)
    major = forms.CharField(max_length=50, help_text='专业或相关专业', required=False)
    school_name = forms.CharField(max_length=50, help_text='毕业院校名称', required=False)

    graduation_time = forms.DateField(help_text="毕业时间", required=False)

    # 资格证件照
    certificate_photos_form = forms.IntegerField(required=False)
    # 毕业证件照
    diploma_certificate_photos_form = forms.IntegerField(required=False)
    person_in_charge = forms.CharField(max_length=50, help_text='单位负责报名的负责人', required=False)
    course_hours = forms.IntegerField(required=False)
    primary_level = forms.CharField(max_length=20, help_text='原级别', required=False)
    former_occupation=forms.CharField(max_length=50, help_text='证书本职业（工种）或相关职业（工种）', required=False)
    student_source_class = forms.IntegerField(required=False)
    identify_subject = forms.IntegerField(required=False)
    identify_class = forms.IntegerField(required=False)
    subside_class = forms.IntegerField(required=False)
    subside_certificate_class = forms.IntegerField(required=False)
    subside_certificate_number = forms.CharField(max_length=20, help_text='证书编号', required=False)
    examinee_identity = forms.IntegerField(required=False)
    place_sign_up = forms.IntegerField(required=False)

    
