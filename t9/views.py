from django.http import HttpResponse
from django.shortcuts import render
from .tasks import first_task, send_email
from .models import Poetry

from .my_singal import action
# Create your views here.

def first_celery(req):
    # 任务函数的异步调用
    first_task.delay(4)
    send_email.delay("liuda@1000phone.com")
    return HttpResponse("ok")


def create_poetry_czn(req):
    p = Poetry()
    p.title = "锄禾"
    p.author = "啊能"
    p.content = "锄禾日当午，种地真辛苦"
    p.save()
    # 发送你自己的信号
    action.send(sender="王老板", param1="晚上十点半", param2="操场见")
    return HttpResponse("搞定")