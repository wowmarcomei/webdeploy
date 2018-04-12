# 继承forms类来创建表单
from django import forms
from django.core.exceptions import ValidationError

# 自定义一个验证器,传递参数是评论本身,评论必须大于4个字节
def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('Not enough words')

# 自定义一个验证器,传递参数是评论本身,评论中不能包含某字符
def chars_validator(comment):
    if 'a' in comment:
        raise ValidationError('not allowed to input that word')

# 创建的CommentForm类被实例化后，一旦被template层引用，django将会自动被创建表单
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    # 传递参数widget使得评论框变成大的输入框,传递参数error_messages为django自带验证器，参数validators为自定义验证器
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'wow,such words'
        },
        validators = [words_validator,chars_validator]
    )
