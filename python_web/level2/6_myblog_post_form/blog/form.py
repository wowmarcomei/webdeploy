# 继承forms类来创建表单
from django import forms

# 创建的CommentForm类被实例化后，一旦被template层引用，django将会自动被创建表单
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField()