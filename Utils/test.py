import requests
import random
from Utils.UAList import UAList

url = 'https://bbs.csdn.net/forums/edi'
ua = random.choice(UAList)
headers = {'User-Agent': ua}
response = requests.get(url=url, headers=headers)

t = response.text

with open('../PageText/' + '1682510390404' + '.html', 'a', encoding='utf-8') as f:
    f.write(t)

