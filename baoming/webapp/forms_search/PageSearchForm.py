from django import forms


class PageSearchForm(forms.Form):
    # 添加分页信息
    page = forms.IntegerField(help_text='页数', required=False)
    per_page = forms.IntegerField(help_text='每页条数', required=False)
