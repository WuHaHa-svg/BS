import json
import atexit

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.utils import timezone

from Spider.models import TaskModel
from Log.models import LogModel
from Utils.PageSave import GetAllSave
from Utils.UrlCheck import UrlCheck
from Utils.TaskCreate import GetTaskList
from datetime import datetime, timedelta, date
from Utils.GetDateResNum import GetDateResNum
from SQL.models import SqlResult
from XSS.models import XssResult
from Utils import Logger


def GetConfig(request):
    if request.method == 'POST':
        # 接收到的数据转换为字典
        data = json.loads(request.body)

        targetURL = data['targetURL']  # 目标URL
        max_depth = data['max_depth']  # 最大检测深度
        is_sql_scan = data['is_sql_scan']  # SQL注入检测开关
        is_xss_scan = data['is_xss_scan']  # XSS注入检测开关
        if not max_depth:  # 如果用户不填写最大检测深度，则默认为最大检测深度为3
            max_depth = 3
        else:
            max_depth = int(max_depth)
        if not is_sql_scan:  # 如果用户不提交SQL注入检测开关，则默认开启
            is_sql_scan = 'Y'
        if not is_xss_scan:  # 如果用户不提交XSS注入检测开关，则默认开启
            is_xss_scan = 'Y'
        targetURL = UrlCheck(targetURL)  # 调用URLCheck方法来校验URL格式，可以自动补全头部协议并验证其是否可请求
        if targetURL == 'EmptyUrl':
            return JsonResponse({'msg': 'TargetURL Is Unavailable！'})

        # print(targetURL, max_depth, is_sql_scan, is_xss_scan)
        res = GetTaskList(targetURL=targetURL, max_depth=max_depth, is_sql_scan=is_sql_scan,
                          is_xss_scan=is_xss_scan)  # 调用GetTaskList方法保存检测任务、页面保存任务
        if res:  # 如果创建任务过程有错误信息，则返回
            response_data = res
            return JsonResponse(response_data)
        response_data = {'msg': 'System Config Complete！'}
        # 调用GetAllSave函数保存所有任务页面标签
        # GetAllSave()
        return JsonResponse(response_data)  # 参数配置处理完毕
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def GetAllTasks(request):
    if request.method == 'GET':
        taskQueryset = TaskModel.objects.all()
        data = serializers.serialize('json', taskQueryset)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def GetSqlTasks(request):
    if request.method == 'GET':
        taskQueryset = TaskModel.objects.filter(is_sql_scan='Y')  # 仅返回开启SQL注入检测的任务
        data = serializers.serialize('json', taskQueryset)  # 数据序列化
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def DelSqlTask(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # 参数处理
        obj = TaskModel.objects.get(id=data['id'])  # 检索任务对象
        obj.is_sql_scan = 'N'  # 关闭SQL注入检测
        obj.save()
        return JsonResponse({'msg': "Task Has Been Delete！"})
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def GetXssTasks(request):
    if request.method == 'GET':
        taskQueryset = TaskModel.objects.filter(is_xss_scan='Y')
        data = serializers.serialize('json', taskQueryset)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def DelXssTask(request):
    if request.method == 'POST':  # 判断请求方法
        data = json.loads(request.body)  # 解析入参
        obj = TaskModel.objects.get(id=data['id'])
        obj.is_xss_scan = 'N'  # 执行删除任务，关闭XSS注入检测开关
        obj.save()
        return JsonResponse({'msg': "Task Has Been Delete！"})
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


def GetRes(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # 参数处理
        s_obj = SqlResult.objects.filter(url=data['url'])  # 检索任务对象
        x_obj = XssResult.objects.filter(url=data['url'])
        res = []
        for item in s_obj:
            res.append(item)
        for item in x_obj:
            res.append(item)
        json_data = serializers.serialize('json', res)
        return JsonResponse(data=json_data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})


# 任务数
def TenDaysTasks(request):
    if request.method == 'GET':
        now = timezone.localtime(timezone.now())
        ten_days_ago = now - timedelta(days=10)
        num_list = []
        for i in range(10):
            start_date = ten_days_ago + timedelta(days=i)
            end_date = start_date + timedelta(days=1)
            time = str(end_date).split(' ')[0]
            sql_objects = TaskModel.objects.filter(
                Q(created_time__gte=start_date) & Q(created_time__lt=end_date) & Q(is_sql_scan='Y'))
            sql_num = len(sql_objects)
            xss_objects = TaskModel.objects.filter(
                Q(created_time__gte=start_date) & Q(created_time__lt=end_date) & Q(is_xss_scan='Y'))
            xss_num = len(xss_objects)
            item = {"time": time, "sqlNum": sql_num, "xssNum": xss_num}
            num_list.append(item)

        data_list = json.dumps(num_list)
        return JsonResponse(data=data_list, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


# 接受任务数
def TenDaysTaskProcNum(request):
    if request.method == 'GET':
        now = timezone.localtime(timezone.now())
        ten_days_ago = now - timedelta(days=10)
        num_list = []
        for i in range(10):
            start_date = ten_days_ago + timedelta(days=i)
            end_date = start_date + timedelta(days=1)
            time = str(end_date).split(' ')[0]
            sql_objects = TaskModel.objects.filter(
                Q(recv_time__gte=start_date) & Q(recv_time__lt=end_date) & Q(is_sql_scan='Y'))
            sql_num = len(sql_objects)

            xss_objects = TaskModel.objects.filter(
                Q(recv_time__gte=start_date) & Q(recv_time__lt=end_date) & Q(is_xss_scan='Y'))
            xss_num = len(xss_objects)
            item = {'time': time, 'sqlNum': sql_num, 'xssNum': xss_num}
            num_list.append(item)

        data_list = json.dumps(num_list)
        return JsonResponse(data=data_list, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


# 漏洞数
def TenDaysResNum(request):
    if request.method == 'GET':
        now = timezone.localtime(timezone.now())
        ten_days_ago = now - timedelta(days=10)
        num_list = []
        for i in range(10):
            start_date = ten_days_ago + timedelta(days=i)
            end_date = start_date + timedelta(days=1)
            time = str(end_date).split(' ')[0]
            sql_objects = SqlResult.objects.filter(task_created_time__gte=start_date,
                                                   task_created_time__lt=end_date)
            sql_num = len(sql_objects)
            xss_objects = XssResult.objects.filter(task_created_time__gte=start_date,
                                                   task_created_time__lt=end_date)
            xss_num = len(xss_objects)
            item = {'time': time, 'sqlNum': sql_num, 'xssNum': xss_num}
            num_list.append(item)

        data_list = json.dumps(num_list)
        return JsonResponse(data=data_list, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


# 漏洞等级分类
def TenDaySqlResGrade(request):
    if request.method == 'GET':
        sql_one = SqlResult.objects.filter(grade='1')
        sql_two = SqlResult.objects.filter(grade='2')
        sql_three = SqlResult.objects.filter(grade='3')
        sql_four = SqlResult.objects.filter(grade='4')
        sql_five = SqlResult.objects.filter(grade='5')
        sql_six = SqlResult.objects.filter(grade='6')
        data = {'sql_one': len(sql_one), 'sql_two': len(sql_two), 'sql_three': len(sql_three),
                'sql_four': len(sql_four), 'sql_five': len(sql_five),
                'sql_six': len(sql_six), }

        return JsonResponse(data=data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


def TenDayXssResGrade(request):
    if request.method == 'GET':
        xss_one = XssResult.objects.filter(grade='1')
        xss_two = XssResult.objects.filter(grade='2')
        xss_three = XssResult.objects.filter(grade='3')
        xss_four = XssResult.objects.filter(grade='4')
        xss_five = XssResult.objects.filter(grade='5')
        xss_six = XssResult.objects.filter(grade='6')
        data = {'sql_one': len(xss_one), 'sql_two': len(xss_two), 'sql_three': len(xss_three),
                'sql_four': len(xss_four), 'sql_five': len(xss_five),
                'sql_six': len(xss_six), }

        return JsonResponse(data=data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


# SqlTasks
def SqlTasks(request):
    if request.method == 'GET':
        INIT = TaskModel.objects.filter(Q(status_sql_scan='INIT') & Q(is_sql_scan='Y'))
        RECV = TaskModel.objects.filter(Q(status_sql_scan='RECV') & Q(is_sql_scan='Y'))
        DONE = TaskModel.objects.filter(Q(status_sql_scan='DONE') & Q(is_sql_scan='Y'))
        data = {'INIT': len(INIT), 'RECV': len(RECV), 'DONE': len(DONE)}
        # data = {'INIT': 32, 'RECV': 6, 'DONE': 231}
        return JsonResponse(data=data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


# XssTasks
def XssTasks(request):
    if request.method == 'GET':
        INIT = TaskModel.objects.filter(Q(status_xss_scan='INIT') & Q(is_xss_scan='Y'))
        RECV = TaskModel.objects.filter(Q(status_xss_scan='RECV') & Q(is_xss_scan='Y'))
        DONE = TaskModel.objects.filter(Q(status_xss_scan='DONE') & Q(is_xss_scan='Y'))
        data = {'INIT': len(INIT), 'RECV': len(RECV), 'DONE': len(DONE)}
        # data = {'INIT': 12, 'RECV': 8, 'DONE': 241}
        return JsonResponse(data=data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed!"})


def TaskHdr(request):
    if request.method == 'GET':
        sqlList = TaskModel.objects.filter(is_sql_scan='Y')
        xssList = TaskModel.objects.filter(is_xss_scan='Y')
        sqlRes = SqlResult.objects.all()
        xssRes = XssResult.objects.all()
        data = {"SqlTask": len(sqlList), "XssTask": len(xssList), "SqlNum": len(sqlRes), "XssNum": len(xssRes)}

        return JsonResponse(data=data, safe=False)
    else:
        return JsonResponse({"msg": "Method Not Allowed！"})
