from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now


# Create your views here.


# def index(request):
#     """进入首页"""
#
#     # 1. 加载模板文件
#     template = loader.get_template('app01/index.html')
#     # 2. 创建请求的上下文:设置界面要显示的数据
#     dict = {}
#     context = RequestContext(request, dict)
#     # 3. 渲染模板:生成标准的html内容
#     html_str = template.render(context)
#     # 4. 响应浏览器:返回 html内容
#     return HttpResponse(html_str)


class Student(object):
    # name = '属性'

    def name(self):
        return '对象中的方法'


def index(request):
    """进入首页"""

    my_dict = {'key01': 'python', 'key02': 'django'}
    my_obj = Student()
    my_list = ['列表1', '列表2', '列表3', '列表4']
    my_date = now()
    my_html = '<font color="red">红色</font>'

    data = {
        'key01': 5,
        'my_dict': my_dict,
        'my_obj': my_obj,
        'my_list': my_list,
        'my_date': my_date,
        'my_html': my_html,
    }

    return render(request, 'app01/index.html', data)


def inherit(request):
    """进入模板继承演示界面"""
    return render(request, 'app01/child.html')


def my_url(request):
    """进入url动态引用演示界面"""
    return render(request, 'app01/my_url.html')


def show_news(request, a, b):
    """
    显示新闻
    :param request:
    :param a: 新闻类别id
    :param b: 第几页
    :return:
    """
    text = '显示新闻： %s  %s' % (a, b)
    return HttpResponse(text)


def show_news2(request, page_no, category):
    """
    显示新闻2
    :param request:
    :param page_no: 新闻类别id
    :param category: 第几页
    :return:
    """
    text = '显示新闻2： %s  %s' % (category, page_no)
    return HttpResponse(text)


def my_reverse(request):
    """进入reverse函数演示界面"""

    # 硬编码:存在维护问题
    # return redirect("/index/")
    # return redirect("/show_news/1/2")
    # return redirect("/show_news2/1/2")

    # 使用reverse函数动态引用
    # url = reverse('app01:index')
    # url = reverse('app01:show_news', args=[1, 2])
    url = reverse('app01:show_news2', kwargs={'category': 1, 'page_no': 2})
    return redirect(url)


# ===============csrf演示(begin)===================
def login(request):
    """进入登录界面"""
    return render(request, 'app01/login.html')


def do_login(request):
    """处理登录操作"""

    # 处理登录操作
    username = request.GET.get('username')
    password = request.GET.get('password')

    if username == 'admin' and password == '123':
        # 登录成功,进入发帖界面
        return redirect('/post/')
    else:
        # 登录失败,回到登录界面
        return redirect('/login/')


def post(request):
    """进入发帖界面"""
    return render(request, 'app01/post.html')


def do_post(request):
    """执行发帖操作"""

    title = request.POST.get('title')
    content = request.POST.get('content')

    text = '成功发表了一篇帖子：%s  %s ' % (title, content)
    return HttpResponse(text)
# ===============csrf演示(end)===================
