import requests
import json
import time


def sqlmapapi(url):
    headers = {  # 数据包里的数据.
        'Content-Type': 'application/json'
    }
    data = {  # 输入扫描的地址.
        'url': url
    }
    task_new_url = 'http://127.0.0.1:8775/task/new'  # 创建任务的URL地址(在IP地址后面加//task/new).  前面的四个就是获取ID信息.
    resp = requests.get(task_new_url)  # 使用get方式请求.
    task_id = resp.json()['taskid']  # 打印json格式下的taskid数据.
    # print(resp.content.decode('utf-8'))              #打印utf-8格式
    if 'success' in resp.content.decode('utf-8'):  # 如果success在resp.content.decode('utf-8')里面
        print('sqlmapapi 创建任务ID成功!')
        scan_task_set_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'  # 添加的是上面创建的新任务ID(/option和/set这二个是固定的.)
        scan_task_set = requests.post(scan_task_set_url, data=json.dumps(data),
                                      headers=headers)  # 使用post方式提交.data=是提交的数据(提交data里面的数据.)
        # print(task_set_resp.content.decode('utf-8'))                                       #打印utf-8格式
        if 'success' in scan_task_set.content.decode(
                'utf-8'):  # 如果success在task_set_resp.content.decode('utf-8')里面设置任务ID的配置
            print('sqlmapapi 设置任务ID的配置成功!')
            task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'  # 添加的是上面创建的新任务ID(/scan和/start是启动对应ID的扫描任务文件.)
            task_start_resp = requests.post(task_start_url, data=json.dumps(data),
                                            headers=headers)  # 使用post方式提交.data=是提交的数据(提交data里面的数据.)
            # print(task_start_resp.content.decode('utf-8'))                                #打印utf-8格式
            if 'success' in task_start_resp.content.decode(
                    'utf-8'):  # 如果success在task_start_resp.content.decode('utf-8')里面
                print('sqlmap 扫描启动成功!')
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'  # 添加的是上面创建的新任务ID(/scan和/status是启动对应ID的扫描任务文件.)
                    task_status_resp = requests.get(task_status_url)  # 使用post方式提交
                    # print(task_status_resp.content.decode('utf-8'))                        #打印utf-8格式
                    if 'running' in task_status_resp.content.decode('utf-8'):  # 还在扫描中
                        print(url + '还在扫描中!')
                        pass
                    else:  # 否则扫描成功!
                        print('sqlmapapi 扫描结束!')
                        task_data_url = 'http://127.0.0.1:8775/scan/' + task_id + '/data'  # 打印data结果.
                        scan_data = requests.get(task_data_url).content.decode('utf-8')  # 使用post方式提交
                        # with open(r'bgxg.txt', 'a+') as f:  # 将结果写到bgxg.txt文件中.
                        #     f.write(url + '\n')
                        #     f.write(scan_data + '\n')
                        #     f.write('下一个数据包' + '\n')
                        #     f.close()
                        print(scan_data)
                        scan_deltask_url = 'http://127.0.0.1:8775/task/' + task_id + '/delete'
                        scan_deltask = requests.get(scan_deltask_url)
                        if 'success' in scan_deltask.content.decode('utf-8'):
                            print('删除 task id 成功')
                        break  # 结束(跳出)
                    time.sleep(3)  # 延迟3秒.


if __name__ == '__main__':

    sqlmapapi(url='http://sqlilab/Less-3/?id=1')