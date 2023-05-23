import re
import requests


def UrlCheck(url, super_url=''):
    res = requests.get(url=url)
    if res.status_code !=200:
        return 'EmptyUrl'
    # 定义正则表达式匹配 URL
    pattern = re.compile(r"(https?://\S+)")
    if re.search(pattern, url):
        if '../' in url:
            u = url.split('/')
            s = super_url.split('/')

            i = min(len(u), len(s))
            for a in range(0, i):
                if u[a] == '..':
                    u[a] = s[a]
            url = ''
            for itme in u:
                url += itme + '/'
            url = url[:-1]
            return url + '/?id=1'
        else:
            return url
    elif len(url) == 0:
        return 'EmptyUrl'
    elif 'javascript' in url:
        return 'EmptyUrl'
    elif 'http' not in url:
        url = super_url + url
        if '../' in url:
            u = url.split('/')
            s = super_url.split('/')
            i = min(len(u), len(s))
            for a in range(0, i):
                if u[a] == '..':
                    u[a] = s[a]
            url = ''
            for itme in u:
                url += itme + '/'
            url = url[:-1]
            return url + '/?id=1'
        else:
            return url + '/?id=1'
