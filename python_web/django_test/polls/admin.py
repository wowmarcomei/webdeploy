from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    # 下面还可以默认多加几个数据
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    # 1. 在admin中对Question类中的数据进行排序，第一个为pub_date字段，第二个为question_text字段
    # fields = ['pub_date','question_text']

    # 2. 将数据分割成多个field
    # fieldsets = [
    #     ('Question information',    {'fields': ['question_text']}),
    #     ('Date information',        {'fields': ['pub_date']}),
    # ]

    # 3. 将数据分割成多个field，且与Choice关联起来
    fieldsets = [
        ('Question information',    {'fields': ['question_text']}),
        ('Date information',        {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # 4.修改显示的所有字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 5.添加filter，字段为pub_date
    list_filter = ['pub_date']

    # 6.添加搜索字段
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)