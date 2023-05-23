import json

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse,HttpResponse
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime, date

from django.utils.datetime_safe import time

# from Utils.GetDateResNum import GetDateResNum
from SQL.models import SqlResult
from XSS.models import XssResult
from django.core import serializers
from Spider.models import TaskModel


def LastTenDayNum(request):
    if request.method == 'GET':
        SqlResNumList = []
        XssResNumList = []
        today = timezone.now()

        # start_time = datetime.combine(today, time.min)
        # end_time = datetime.combine(today, time.max)
        for i in range(10):
            day = today - timezone.timedelta(days=i)
            start_time = datetime.combine(day, datetime.min.time())
            end_time = datetime.combine(day, datetime.max.time())
            start_time = make_aware(start_time)
            end_time = make_aware(end_time)
            sql_results = SqlResult.objects.all()
            m = len(sql_results)
            time = str(start_time).split(' ')[0]
            sql_dic = {time: m}
            SqlResNumList.append(sql_dic)
            xss_results = XssResult.objects.all()
            m = len(sql_results)
            time = str(start_time).split(' ')[0]
            xss_dic = {time: m}
            SqlResNumList.append(xss_dic)
            # SqlResNumList.append(GetDateResNum(model=SqlResult, start_time=start_time, end_time=end_time))
            # XssResNumList.append(GetDateResNum(model=XssResult, start_time=start_time, end_time=end_time))
        data = {
            "sql": SqlResNumList,
            "xss": XssResNumList
        }
        # response = JsonResponse(data,safe=False)

        return HttpResponse("200")
