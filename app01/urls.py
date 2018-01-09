from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

urlpatterns = [

    # 进入首页
    url(r'^indexaa/$', views.index, name='index'),
    # 进入模板继承演示界面
    url(r'^inherit/$', views.inherit),
    # 进入url动态引用演示界面
    url(r'^my_url/$', views.my_url),

    # 进入reverse函数演示界面
    url(r'^my_reverse/$', views.my_reverse),


    # 位置参数：http://127.0.0.1:8000/show_news/10/2/
    url(r'^show_newsaa/(\d+)/(\d+)/$', views.show_news, name='show_news'),
    # 关键字参数：http://127.0.0.1:8000/show_news2/10/2/
    url(r'^show_news2aa/(?P<category>\d+)/(?P<page_no>\d+)/$',
        views.show_news2, name='show_news2'),


    # =========csrf演示(begin)==========
    # 进入登录界面
    url(r'^login/$', views.login),
    # 处理登录操作
    url(r'^do_login/$', views.do_login),
    # 进入发帖界面
    url(r'^post/$', views.post),
    # 处理发帖操作
    url(r'^do_post/$', views.do_post),
    # =========csrf演示(end)==========
]
