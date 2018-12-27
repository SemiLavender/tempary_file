import json
import os
import re

urllist = ["http://baidu.com",
           "http://www.qq.com",
           "http://www.sina.com.cn/"]


# 这个函数主要是构造出一个特定格式的字典，用于zabbix
def web_site_discovery():
    web_list = []
    web_dict = {"data": None}

    for url in urllist:
        url_dict = {}
        url_dict["{#SITENAME}"] = url
        web_list.append(url_dict)

    web_dict["data"] = web_list
    jsonStr = json.dumps(web_dict, sort_keys=True, indent=4)
    print(jsonStr)

web_site_discovery()
