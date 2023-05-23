import json

from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from Spider.models import TaskModel
from .SqlInjector import Injection
from .signals import task_start
from Log.models import LogModel
from SQL.payload import SQLInjection
from SQL.models import SqlResult
from Utils.ThreadingSqlTasks import TaskSubmit
import random
import requests


# Create your views here.


def SqlTaskStart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = TaskModel.objects.get(id=data['id'])
        # 如果任务已经是开启状态
        if obj.status_sql_scan != "INIT":
            return JsonResponse({"msg": "该任务已经开始，请勿重复操作！"})
        # 修改任务状态为已接受
        obj.status_sql_scan = "RECV"
        obj.recv_time = timezone.now()
        obj.save()
        # 先返回任务开始成功响应，再利用信号task_start执行任务，由信号函数调用Injection方法
        task_start.send(sender=SqlTaskStart, TaskModelObj=obj)
        # Injection(TaskModelObj=obj)
        res = {"msg": "任务开始！"}
        return JsonResponse(res)


def AllSqlStart(request):
    if request.method == 'GET':
        # 检索全部开启SQL注入并且状态处于刚生成阶段的任务对象
        task_list = TaskModel.objects.filter(Q(is_sql_scan='Y') & Q(status_sql_scan='INIT'))
        # 如果检索不到开启SQL注入并且状态处于刚生成阶段的任务对象，就返回
        if len(task_list) == 0:
            return JsonResponse({'msg': "No SQLInjection Tasks！"})
        # 创建任务池
        SqlTaskList = []
        for task in task_list:
            SqlTaskList.append(task)
        # 将任务池提交给多线程处理方法，后台执行任务，先返回成功响应
        TaskSubmit(task_list=SqlTaskList)
        return JsonResponse({'msg': "The SQLInjection Tasks Has Been Received！"})


def GetInfo(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # 接收数据并处理
        obj = TaskModel.objects.get(id=data['id'])
        son_obj_set = TaskModel.objects.filter(
            Q(super_url=obj.url) & Q(is_sql_scan='Y'))  # 过滤出上级url等于此任务url并且开启了SQL注入检测的子任务
        son_num = len(son_obj_set)  # 将son_num赋值
        data = serializers.serialize('json', [obj])  # 将对象序列化
        data = (data[0:-3])
        data = data + ', "son_num": {}'.format(son_num) + "}}]"  # 将son_num添加到json字串
        return JsonResponse(data, safe=False)


def SqlDelSon(request):
    if request.method == 'POST':
        data = json.loads(request.body)     #处理数据请求
        if data['type'] != 'sqlScan':       #如果前端提交的任务类型不是SQL注入任务就返回错误信息，sql注入任务只能关闭SQL注入子任务
            return JsonResponse({"msg": "Interface Error!"})
        print(data['taskUrl'])
        objLst = TaskModel.objects.filter(Q(super_url=data['taskUrl']) & Q(is_sql_scan='Y'))    #检索此任务的SQL注入子任务
        print(objLst)
        for item in objLst:
            item.is_sql_scan = 'N'      #关闭SQL注入检测任务开关
            item.save()
        res = {"msg": "子任务已删除！"}    #返回成功信息
        return JsonResponse(res)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})
