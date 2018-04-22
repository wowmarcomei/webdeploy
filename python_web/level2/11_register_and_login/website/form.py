# 构造登陆表单
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    