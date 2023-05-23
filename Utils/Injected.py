import json

import requests


def scan(url, id, header):
    data = {'url': url}
    task_set_url = 'http://127.0.0.1:8775/option/' + id + '/set'
    res = requests.post(task_set_url, data=json.dumps(data), headers=header)
    if 'success' in res.content.decode('utf-8'):
        print('scan start success')
    while 1:
        task_status_url = 'http://127.0.0.1:8775/scan/' + id + '/status'
        task_status_res = requests.get(task_status_url)
        if ('running' in task_status_res.content.decode('utf-8')):
            pass
        else:
            task_data_url = 'http://127.0.0.1:8775/scan/' + id + '/data'
            task_data_res = requests.get(task_data_url).text
            print(id, task_data_res)
            break


scan(url='http://testphp.vulnweb.com/artists.php?artist=1', id='c8cf19c306e664a0', header={
    'Content-Type': 'application/json'
})
