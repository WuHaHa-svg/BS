import json

import requests


def NewTask():
    res = requests.get('http://127.0.0.1:8775/task/new')
    taskId = res.json()['taskid']
    return taskId


def SetTask(taskId, url):
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        "url": url
    }
    task_set_url = 'http://127.0.0.1:8775/option/' + taskId + '/set'
    task_set_res = requests.post(task_set_url, data=json.dumps(data), headers=header)
    if 'success' in task_set_res.content.decode('utf-8'):
        print('setting success')


def StartScan(taskId, url):
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        "url": url + "/?id="
    }
    task_start_url = 'http://127.0.0.1:8775/scan/' + taskId + '/start'
    task_start_res = requests.post(task_start_url, data=json.dumps(data), headers=header)
    if ('success' in task_start_res.content.decode('utf-8')):
        print('scan start success')


def GetResult(taskId):
    while 1:
        task_status_url = 'http://127.0.0.1:8775/scan/' + taskId + '/status'
        task_status_res = requests.get(task_status_url)
        if ('running' in task_status_res.content.decode('utf-8')):
            # print('sqlmap are running  ')
            pass
        else:
            task_data_url = 'http://127.0.0.1:8775/scan/' + taskId + '/data'
            task_data_res = requests.get(task_data_url).text
            res_list = json.loads(task_data_res)['data'][1]['value'][0]['data']
            FreeTask(taskId)
            return res_list


def FreeTask(taskId):
    scan_deltask_url = 'http://127.0.0.1:8775/task/' + taskId + '/delete'
    scan_deltask = requests.get(scan_deltask_url)
    return scan_deltask
