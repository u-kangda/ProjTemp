from django.template.base import Library

# 名字不能修改
register = Library()


@register.filter
def odd(value):
    """
    过滤器: 判断是否为奇数
    :param value: 模板变量
    :return:
    """
    return value % 2 == 1


@register.filter
def mod(value, param):
    """
    过滤器:求余操作
    :param value: 模板变量
    :param param: 除数
    :return:
    """
    return value % param






