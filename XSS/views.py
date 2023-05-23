import json

from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from Spider.models import TaskModel
from .XssInjector import Injection
from XSS.signals import task_start
from Log.models import LogModel
from Utils.ThreadingXssTasks import TaskSubmit
import random
import requests


# Create your views here.


def XssTaskStart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = TaskModel.objects.get(id=data['id'])
        if obj.status_xss_scan != "INIT":
            return JsonResponse({"msg": "该任务已经开始，请勿重复操作！"})
        obj.status_xss_scan = "RECV"
        obj.recv_time = timezone.now()
        obj.save()
        # 先返回任务开始成功响应，再利用信号task_start执行任务
        task_start.send(sender=XssTaskStart, TaskModelObj=obj)
        res = {"msg": "任务开始！"}
        return JsonResponse(res)


def AllXssStart(request):
    if request.method == 'GET':
        task_list = TaskModel.objects.filter(Q(is_xss_scan='Y') and Q(status_xss_scan='INIT'))      #检索出全部的未开始XSS注入检测的XSS检测任务
        if len(task_list) == 0:
            return JsonResponse({'msg': "No XSSInjection Tasks！"})
        XssTaskList = []            #定义XSS检测任务池
        for task in task_list:
            XssTaskList.append(task)
        TaskSubmit(task_list=XssTaskList)       #任务池提交到线程池处理
        return JsonResponse({'msg': "All The XSSInjection Tasks Has Been Received！"})


def GetInfo(request):
    if request.method == 'POST':    #判断请求方法
        data = json.loads(request.body)
        obj = TaskModel.objects.get(id=data['id'])  #获取相应的任务对象
        son_obj_set = TaskModel.objects.filter(Q(super_url=obj.url) & Q(is_xss_scan='Y'))       #获取子任务的队列
        son_num = len(son_obj_set)              #为子任务数son_num赋值
        data = serializers.serialize('json', [obj])         #任务对象序列化
        data = (data[0:-3])                         #a将son_num添加到json字串
        data = data + ', "son_num": {}'.format(son_num) + "}}]"
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"msg":"Method Not Allowed"})


def XssDelSon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['type'] != 'xssScan':
            return JsonResponse({"msg": "Interface Error!"})
        print(data['taskUrl'])
        objLst = TaskModel.objects.filter(Q(super_url=data['taskUrl']) & Q(is_xss_scan='Y'))
        print(objLst)
        for item in objLst:
            item.is_xss_scan = 'N'
            item.save()
        res = {"msg": "子任务已删除！"}
        return JsonResponse(res)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})
