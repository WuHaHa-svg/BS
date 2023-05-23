import time
from django.utils import timezone
from Utils.DATABASE import CONN
from Utils.UAList import UAList
import requests
import random


def GetAllSave():
    sql = 'SELECT * FROM spider_savemodel'
    cursor = CONN.cursor()
    cursor.execute(sql)

    # 获取查询结果
    results = cursor.fetchall()
    CONN.commit()
    cursor.close()

    # 查询结果
    for row in results:
        SaveText(row)
        # time.sleep()


def SaveText(row):
    # UA伪装
    ua = random.choice(UAList)
    cursor = CONN.cursor()
    log_id = str(int(time.time() * 1000))
    try:
        headers = {'User-Agent': ua}
        response = requests.get(url=row['url'], headers=headers)
        text = response.text
        # 保存标签数据
        src = 'E:/BS/BS/PageText/' + row['id'] + '.txt'
        with open(src, 'a', encoding='utf-8') as f:
            f.write(text)

        sql = "UPDATE spider_savemodel SET is_save = 'Y' WHERE id = {}".format(row['id'])
        cursor.execute(sql)
        # CONN.commit()

        message = '任务URL："{}"，标签保存成功！'.format(row['url'])
        cursor.execute("INSERT INTO log_logmodel (id,message) VALUES (%s,%s)", (log_id, message))
        CONN.commit()
    except:
        sql = "UPDATE spider_savemodel SET is_save = 'E' WHERE id = {}".format(row['id'])
        cursor.execute(sql)
        # CONN.commit()

        message = '任务URL："{}"，标签保存失败！'.format(row['url'])
        cursor.execute("INSERT INTO log_logmodel (id,message) VALUES (%s,%s)", (log_id, message))
        CONN.commit()
