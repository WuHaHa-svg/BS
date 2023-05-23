import concurrent.futures
from time import sleep

from django.utils import timezone

from XSS.models import XssResult
from Utils.SqlScanner import NewTask, SetTask, StartScan, GetResult


# 定义任务函数
def Task(task_item):
    task = NewTask()
    SetTask(task, task_item.url)
    StartScan(task, task_item.url)
    res_list = GetResult(task)
    if len(res_list) == 0:
        res = XssResult()
        res.url = task_item.url
        res.type = "null"
        res.title = "null"
        res.injection = "null"
        res.task_created_time = task_item.created_time
        res.task_begin_time = task_item.recv_time
        res.task_end_time = timezone.now()
        res.save()
    else:
        for item in res_list.values():
            res = XssResult()
            res.url = task_item.url
            res.type = 'XssInjection'
            res.title = item['title']
            res.injection = item['payload']
            res.task_created_time = task_item.created_time
            res.task_begin_time = task_item.recv_time
            res.task_end_time = timezone.now()
            res.save()
    task_item.status_sql_scan = 'DONE'
    task_item.end_time = timezone.now()
    task_item.save()


# 提交任务到线程池
def TaskSubmit(task_list):
    # 创建线程池，线程池容量为5
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    for task_item in task_list:
        thread_pool.submit(Task, task_item)
        task_item.status_xss_scan = 'RECV'      #任务接受状态
        task_item.recv_time = timezone.now()       #任务接受时间
        task_item.save()
    # 不要等待所有任务完成，任务后台执行，前台先结束函数
    thread_pool.shutdown(wait=False)
