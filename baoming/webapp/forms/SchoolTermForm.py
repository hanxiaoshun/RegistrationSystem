from django import forms


class SchoolTermForm(forms.Form):
    """
    报名周期管理
    """
    school_term_start = forms.DateField(help_text="报名学期开始", required=False)
    school_term_end = forms.DateField(help_text="报名学期结束", required=False)
    explain = forms.CharField(max_length=150, help_text='本报名周期的说明文件', required=False)
