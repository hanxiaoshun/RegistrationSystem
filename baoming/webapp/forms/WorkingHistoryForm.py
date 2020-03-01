from django import forms


class WorkingHistoryForm(forms.Form):
    # 修改所需
    obj_id = forms.IntegerField()

    start_year = forms.IntegerField(help_text='起始年')
    start_month = forms.IntegerField(help_text='起始月')
    end_year = forms.IntegerField(help_text='结束年')
    end_month = forms.IntegerField(help_text='结束月')
    unit_name = forms.CharField(help_text='单位名称')
    hukou_province_form = forms.IntegerField()
    hukou_city_form = forms.IntegerField()
    hukou_county_form = forms.IntegerField()
    job_content = forms.CharField(help_text='岗位工作简介')
