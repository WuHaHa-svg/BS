#! /usr/bin/env python
# coding=utf-8
import json
import time
import requests


def creat_task(url, data, cookie=''):
    json_data = json.dumps({'url': url, 'data': data, 'cookie': cookie})
    req = requests.post('http://127.0.0.1:2333/xssfork/create_task/7T2o22NcQSLGk75', data=json_data,
                        headers={'Content-Type': 'application/json'})
    return req.content


def start_task(task_id):
    req = requests.get('http://127.0.0.1:2333/xssfork/start_task/7T2o22NcQSLGk75/{}'.format(task_id))
    return req.content


def get_task_status(task_id):
    req = requests.get('http://127.0.0.1:2333/xssfork/task_status/7T2o22NcQSLGk75/{}'.format(task_id))
    return req.content


def get_task_result(task_id):
    req = requests.get('http://127.0.0.1:2333/xssfork/task_result/7T2o22NcQSLGk75/{}'.format(task_id))
    return req.content


def running(task_id):
    time.sleep(5)
    task_status = int(json.loads(get_task_status(task_id)).get('status'))
    return task_status in [0, 1]


if __name__ == "__main__":
    url = "http://127.0.0.1/xss-labs/level1.php"
    data = "name=test"
    # cookie = "usid=admin"
    task_id = json.loads(creat_task(url, data)).get('task_id')
    start_task(task_id)
    while True:
        res = get_task_status(task_id)
        print(res)
        if 'task has been done' in str(res):
            break
    print(get_task_result(task_id))
