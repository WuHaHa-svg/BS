import json

import requests


def NewTask():
    res = requests.get('http://127.0.0.1:8775/task/new')
    taskId = res.json()['taskid']
    return taskId


def StartScan(taskId, url):
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        "url": url
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
            return res_list
