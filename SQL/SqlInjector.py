import time
import requests
import json
from django.utils import timezone

import threading
from Spider.models import TaskModel
from SQL.models import SqlResult
from Utils import SqlScanner


def Injection(TaskModelObj, **kwargs):
    print("============Infsdgfds==========")
    task = SqlScanner.NewTask()  # 创建新的检测节点
    SqlScanner.SetTask(task, TaskModelObj.url)
    SqlScanner.StartScan(task, TaskModelObj.url)  # 开始检测任务
    print(task,TaskModelObj.url)
    res_list = SqlScanner.GetResult(task)  # 获取检测结果
    # print(task,":",res_list)
    for grade, item in res_list.items():  # 保存检测结果
        res = SqlResult()
        res.url = TaskModelObj.url
        res.type = 'SqlInjection'
        res.grade = grade
        res.title = item['title']
        res.injection = item['payload']
        res.task_created_time = TaskModelObj.created_time
        res.task_begin_time = TaskModelObj.recv_time
        res.task_end_time = timezone.now()
        res.save()
    # 修改任务状态
    TaskModelObj.status_sql_scan = 'DONE'
    TaskModelObj.end_time = timezone.now()
    TaskModelObj.save()
