from django import template
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

register = template.Library()
# 这是定义模板标签要用到的

@register.simple_tag(takes_context=True)
# 这个装饰器表明这个函数是一个模板标签，takes_context = True 表示接收上下文对象，就是前面所说的封装了各种变量的 Context 对象。
def paginate(context,object_list,page_count):
    """
    # context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量
    """
    left = 3 # 当前页码左边显示几个页码号 -1，比如3就显示2个
    right =3 # 当前页码右边显示几个页码号 -1

    paginator = Paginator(object_list,page_count) # 通过object_list分页对象
    page = context['request'].GET.get('page') # 从 Http 请求中获取用户请求的页码号

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)
        pages = get_left(context['current_page'], left, paginator.num_pages) + get_right(context['current_page'], right,
                                                                                         paginator.num_pages)
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
        pages = get_right(context['current_page'], right, paginator.num_pages)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages
        pages = get_left(context['current_page'], left, paginator.num_pages)

    context['article_list'] = object_list
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    try:
        context['pages_first'] = pages[0]
        context['pages_last'] = pages[-1] + 1
    except IndexError:
        context['pages_first'] = 1
        context['pages_last'] = 2

    return ''  # 必须加这个，否则首页会显示个None

def get_left(current_page, left, num_pages):
    """
        辅助函数，获取当前页码的值得左边两个页码值，要注意一些细节，比如不够两个那么最左取到2，为了方便处理，
        包含当前页码值，比如当前页码值为5，那么pages = [3,4,5]
    """
    if current_page == 1:
        return []
    elif current_page == num_pages:
        l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
        l.sort()
        return l
    l = [i for i in range(current_page, current_page - left, -1) if i > 1]
    l.sort()
    return l


def get_right(current_page, right, num_pages):
    """
        辅助函数，获取当前页码的值得右边两个页码值，要注意一些细节，比如不够两个那么最右取到最大页码值。不包含当前页码值。
        比如当前页码值为5，那么pages = [6,7]
    """
    if current_page == num_pages:
        return []
    return [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]



