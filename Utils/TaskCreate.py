import requests
import random
from lxml import etree
from django.utils import timezone
from Spider.models import TaskModel
from Utils.UrlCheck import UrlCheck
from Utils.UAList import UAList


# 获取targetURL子url列表并创建任务
def GetTaskList(targetURL, max_depth, is_sql_scan, is_xss_scan, depth=0, super_url=''):  # 当前深度depth默认为0
    # 如果深度超出定义深度就结束
    if max_depth == 0:
        targetURL = UrlCheck(targetURL)
        task = TaskModel(url=targetURL, is_sql_scan=is_sql_scan, is_xss_scan=is_xss_scan, depth=0, max_depth=max_depth)
        task.created_time = timezone.now()
        task.save()
        return
    if depth > (max_depth - 1):
        return
    if depth == 0:
        # 创建检测任务
        targetURL = UrlCheck(targetURL)
        task = TaskModel(url=targetURL, is_sql_scan=is_sql_scan, is_xss_scan=is_xss_scan, depth=0, max_depth=max_depth)
        task.created_time = timezone.now()
        task.save()
    # 获取目标URL的当前页面上的URL：
    url = targetURL
    # UA伪装，防止目标URL所在服务器限制爬虫模块频繁发起的请求
    ua = random.choice(UAList)
    try:
        headers = {'User-Agent': ua}
        response = requests.get(url=url, headers=headers)
    except:
        return {'msg': 'URL Not Available！'}
    page = response.content
    tree = etree.HTML(page)
    # 如果此页面有标签：
    if len(tree) > 0:
        # 提取本页面所有的URL
        lst = tree.xpath('//@href')
        # 保存本页面所有的URL
        for url in lst:
            print("url:", url)
            print("targetURL:", targetURL)
            url = UrlCheck(url, targetURL)

            if url != 'EmptyUrl':
                task = TaskModel(url=url, is_sql_scan=is_sql_scan, is_xss_scan=is_xss_scan, depth=depth + 1,
                                 # 当前深度的depth加一
                                 max_depth=max_depth, super_url=targetURL)
                task.created_time = timezone.now()
                task.save()
                GetTaskList(url, max_depth=max_depth, is_sql_scan=is_sql_scan, is_xss_scan=is_xss_scan,
                            depth=depth + 1)  # 继续请求本页面上的URL
