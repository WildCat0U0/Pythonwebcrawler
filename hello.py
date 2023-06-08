import re
import json
import random
import pandas as pd
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

mapping = {
    1 : "🟊",
    2 : "🟊🟊",
    3 : "🟊🟊🟊",
    4 : "🟊🟊🟊🟊",
    5 : "🟊🟊🟊🟊🟊"
}

for i in range(0, 70):
    url_good = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0" \
               "&t=1686206911945&loginType=3&uuid=122270672.16854216029861357898847.1685421603.1685449329.1686205630.3" \
               f"&productId=100038004389&score=3&sortType=5&page={i}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield="
    url_middle = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0" \
                 "&t=1686206911945&loginType=3&uuid=122270672.16854216029861357898847.1685421603.1685449329.1686205630.3" \
                 f"&productId=100038004389&score=2&sortType=5&page={i}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield="
    url_bad = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0" \
              "&t=1686206669984&loginType=3&uuid=122270672.16854216029861357898847.1685421603.1685449329.1686205630.3" \
              f"&productId=100038004389&score=1&sortType=5&page={i}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield="

    response = requests.get(url_good)
    response.encoding = 'gbk'
    html = response.text
    html = json.loads(html)
    html = html['comments']
    for i in html:
        i["content"] = i["content"].replace("\n", ";")
        # strings = list(map(lambda x: mapping[x], i["score"]))
        strings = mapping.get(i["score"])
        data = [str(i["id"]), str(i["creationTime"]), strings, str(i["content"])]
        data = pd.DataFrame(data).T
        data.to_csv('result_good.csv', mode='a', index=False, header=False, encoding='utf-8-sig')

    response = requests.get(url_middle)
    response.encoding = 'gbk'
    html = response.text
    html = json.loads(html)
    html = html['comments']
    for i in html:
        i["content"] = i["content"].replace("\n", ";")
        # strings = list(map(lambda x: mapping[x], i["score"]))
        strings = mapping.get(i["score"])
        data = [str(i["id"]), str(i["creationTime"]), strings, str(i["content"])]
        data = pd.DataFrame(data).T
        data.to_csv('result_middle.csv', mode='a', index=False, header=False, encoding='utf-8-sig')

    response = requests.get(url_bad)
    response.encoding = 'gbk'
    html = response.text
    html = json.loads(html)
    html = html['comments']
    for i in html:
        i["content"] = i["content"].replace("\n", ";")
        # strings = list(map(lambda x: mapping[x], i["score"]))
        strings = mapping.get(i["score"])
        data = [str(i["id"]), str(i["creationTime"]), strings, str(i["content"])]
        data = pd.DataFrame(data).T
        data.to_csv('result_bad.csv', mode='a', index=False, header=False, encoding='utf-8-sig')

