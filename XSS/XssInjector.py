import time
import requests
import json
from django.utils import timezone

import threading
from Spider.models import TaskModel
from XSS.models import XssResult
from Utils.SqlScanner import NewTask
from Utils.SqlScanner import SetTask
from Utils.SqlScanner import StartScan
from Utils.SqlScanner import GetResult


def Injection(TaskModelObj, **kwargs):
    task = NewTask()
    SetTask(task, TaskModelObj.url)
    StartScan(task, TaskModelObj.url)
    while True:         #创建死循环监听任务检测结果
        res_list = GetResult(task)
        if res_list.status != 'processing':     #如果任务已经处理完毕
            for grade, item in res_list.items():  # 保存检测结果
                res = XssResult()
                res.url = TaskModelObj.url
                res.type = 'SqlInjection'
                res.grade = grade
                res.title = item['title']
                res.injection = item['payload']
                res.task_created_time = TaskModelObj.created_time
                res.task_begin_time = TaskModelObj.recv_time
                res.task_end_time = timezone.now()
                res.save()
            break           #结果保存完毕，退出循环
    #更改任务状态
    TaskModelObj.status_xss_scan = 'DONE'
    TaskModelObj.end_time = timezone.now()
    TaskModelObj.save()
