## 完整代码

```python
url = "http://tianqi.2345.com/Pc/GetHistory"

headers = {
"User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"""
}

import requests
import pandas as pd

def craw_table(year, month):
    params = {
        "areaInfo[areaId]": 58362,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=headers, params=params)
    #网页的返回内容的类型是str类型的，如果它符合JSON格式，则可以使用json( )方法将其转换为字典类型，以方便解析。
    data = resp.json()["data"]
    df = pd.read_html(data)[0]
    return df


df_list = []
for year in range(2011,2022):
    for month in range(1,13):
        print("爬取：",year,month)
        df = craw_table(year,month)
        df_list.append(df)

pd.concat(df_list).to_excel("上海2011-2021年天气数据.xlsx", index=False)
```

## 优化后，封装方法，上海2011年-2021年天气数据

```python
import requests
import pandas as pd

url = "http://tianqi.2345.com/Pc/GetHistory"
headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"""
}

df_list = []


def craw_table(year, month):
    params = {
        "areaInfo[areaId]": 58362,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=headers, params=params)
    #网页的返回内容的类型是str类型的，如果它符合JSON格式，则可以使用json( )方法将其转换为字典类型，以方便解析。
    data = resp.json()["data"]
    df = pd.read_html(data)[0]
    return df


# 主方法
def main():
    for year in range(2011, 2022):
        for month in range(1, 13):
            print("爬取：", year, month)
            df = craw_table(year, month)
            df_list.append(df)

    pd.concat(df_list).to_excel("上海2011年-2021年天气数据.xlsx", index=False)


if __name__ == '__main__':
    main()

```



print(resp.text)得到

```html

{
"code":1,
"msg":"",
"data":"<ul class=\"history-msg\">\n    <li>\u5e73\u5747\u9ad8\u6e29\uff1a<em class=\"orange-txt\">9\u00b0<\/em>&nbsp;&nbsp;&nbsp;&nbsp;\u5e73\u5747\u4f4e\u6e29\uff1a<em class=\"blue-txt\">3\u00b0<\/em><\/li>\n    <li>\u6781\u7aef\u9ad8\u6e29\uff1a<em class=\"orange-txt\">19\u00b0<\/em><b>(2021-01-15)<\/b><\/li>\n    <li>\u6781\u7aef\u4f4e\u6e29\uff1a<em class=\"blue-txt\">-6\u00b0<\/em><b>(2021-01-07)<\/b><\/li>\n        <li>\u5e73\u5747\u7a7a\u6c14\u8d28\u91cf\u6307\u6570\uff1a<em class=\"blod-txt\">63<\/em><\/li>\n    <li>\u7a7a\u6c14\u6700\u597d\uff1a<em class=\"green-txt\">34 \u4f18<\/em><b>(01\u670820\u65e5)<\/b><\/li>\n    <li>\u7a7a\u6c14\u6700\u5dee\uff1a<em class=\"yellow-txt\">97\u826f<\/em><b>(01\u670828\u65e5)<\/b><\/li>\n    <\/ul>\n<table class=\"history-table\" width=\"100%\">\n    <tr>\n        <th width=\"169\">\u65e5\u671f<\/th>\n        <th width=\"68\">\u6700\u9ad8\u6e29<\/th>\n        <th width=\"68\">\u6700\u4f4e\u6e29<\/th>\n        <th width=\"122\">\u5929\u6c14<\/th>\n        <th>\u98ce\u529b\u98ce\u5411<\/th>\n        <th width=\"140\">\u7a7a\u6c14\u8d28\u91cf\u6307\u6570<\/th>    <\/tr>\n        <tr>\n        <td>2021-01-01 \u5468\u4e94<\/td>\n        <td style=\"color:#ff5040;\">4\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-1\u00b0<\/td>\n        <td>\u6674~\u591a\u4e91<\/td>\n        <td>\u897f\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">52 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-02 \u5468\u516d<\/td>\n        <td style=\"color:#ff5040;\">7\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >1\u00b0<\/td>\n        <td>\u6674~\u591a\u4e91<\/td>\n        <td>\u4e1c\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">69 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-03 \u5468\u65e5<\/td>\n        <td style=\"color:#ff5040;\">10\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >6\u00b0<\/td>\n        <td>\u9634<\/td>\n        <td>\u4e1c\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">66 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-04 \u5468\u4e00<\/td>\n        <td style=\"color:#ff5040;\">13\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >7\u00b0<\/td>\n        <td>\u9634<\/td>\n        <td>\u4e1c\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">44 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-05 \u5468\u4e8c<\/td>\n        <td style=\"color:#ff5040;\">8\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >2\u00b0<\/td>\n        <td>\u9634~\u591a\u4e91<\/td>\n        <td>\u4e1c\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">49 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-06 \u5468\u4e09<\/td>\n        <td style=\"color:#ff5040;\">5\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-4\u00b0<\/td>\n        <td>\u9634<\/td>\n        <td>\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">46 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-07 \u5468\u56db<\/td>\n        <td style=\"color:#ff5040;\">-3\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-6\u00b0<\/td>\n        <td>\u9634<\/td>\n        <td>\u897f\u5317\u98ce4\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">67 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-08 \u5468\u4e94<\/td>\n        <td style=\"color:#ff5040;\">-1\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-5\u00b0<\/td>\n        <td>\u9634~\u6674<\/td>\n        <td>\u897f\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">50 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-09 \u5468\u516d<\/td>\n        <td style=\"color:#ff5040;\">3\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-1\u00b0<\/td>\n        <td>\u6674~\u591a\u4e91<\/td>\n        <td>\u897f\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">57 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-10 \u5468\u65e5<\/td>\n        <td style=\"color:#ff5040;\">5\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-1\u00b0<\/td>\n        <td>\u9634~\u591a\u4e91<\/td>\n        <td>\u897f\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">73 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-11 \u5468\u4e00<\/td>\n        <td style=\"color:#ff5040;\">6\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-1\u00b0<\/td>\n        <td>\u591a\u4e91~\u6674<\/td>\n        <td>\u897f\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">70 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-12 \u5468\u4e8c<\/td>\n        <td style=\"color:#ff5040;\">8\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >1\u00b0<\/td>\n        <td>\u6674<\/td>\n        <td>\u897f\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">94 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-13 \u5468\u4e09<\/td>\n        <td style=\"color:#ff5040;\">14\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >4\u00b0<\/td>\n        <td>\u6674<\/td>\n        <td>\u897f\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">80 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-14 \u5468\u56db<\/td>\n        <td style=\"color:#ff5040;\">16\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >6\u00b0<\/td>\n        <td>\u591a\u4e91~\u6674<\/td>\n        <td>\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">80 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-15 \u5468\u4e94<\/td>\n        <td style=\"color:#ff5040;\">19\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >2\u00b0<\/td>\n        <td>\u6674~\u9634<\/td>\n        <td>\u897f\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">80 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-16 \u5468\u516d<\/td>\n        <td style=\"color:#ff5040;\">7\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >0\u00b0<\/td>\n        <td>\u9634~\u591a\u4e91<\/td>\n        <td>\u4e1c\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">73 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-17 \u5468\u65e5<\/td>\n        <td style=\"color:#ff5040;\">5\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >-1\u00b0<\/td>\n        <td>\u9634~\u6674<\/td>\n        <td>\u897f\u5317\u98ce\u5fae\u98ce<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">62 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-18 \u5468\u4e00<\/td>\n        <td style=\"color:#ff5040;\">11\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >2\u00b0<\/td>\n        <td>\u6674<\/td>\n        <td>\u897f\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">84 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-19 \u5468\u4e8c<\/td>\n        <td style=\"color:#ff5040;\">11\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >6\u00b0<\/td>\n        <td>\u591a\u4e91~\u6674<\/td>\n        <td>\u4e1c\u5357\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">68 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-20 \u5468\u4e09<\/td>\n        <td style=\"color:#ff5040;\">13\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >12\u00b0<\/td>\n        <td>\u591a\u4e91~\u9634<\/td>\n        <td>\u4e1c\u5357\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">34 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-21 \u5468\u56db<\/td>\n        <td style=\"color:#ff5040;\">17\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >9\u00b0<\/td>\n        <td>\u9634~\u5c0f\u96e8<\/td>\n        <td>\u4e1c\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">46 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-22 \u5468\u4e94<\/td>\n        <td style=\"color:#ff5040;\">11\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >7\u00b0<\/td>\n        <td>\u5c0f\u96e8<\/td>\n        <td>\u4e1c\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">64 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-23 \u5468\u516d<\/td>\n        <td style=\"color:#ff5040;\">8\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >4\u00b0<\/td>\n        <td>\u5c0f\u96e8~\u9634<\/td>\n        <td>\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">61 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-24 \u5468\u65e5<\/td>\n        <td style=\"color:#ff5040;\">10\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >7\u00b0<\/td>\n        <td>\u9634<\/td>\n        <td>\u4e1c\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">84 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-25 \u5468\u4e00<\/td>\n        <td style=\"color:#ff5040;\">15\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >9\u00b0<\/td>\n        <td>\u9634~\u5c0f\u96e8<\/td>\n        <td>\u4e1c\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">36 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-26 \u5468\u4e8c<\/td>\n        <td style=\"color:#ff5040;\">10\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >6\u00b0<\/td>\n        <td>\u5c0f\u96e8~\u591a\u4e91<\/td>\n        <td>\u897f\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">43 \u4f18<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-27 \u5468\u4e09<\/td>\n        <td style=\"color:#ff5040;\">10\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >4\u00b0<\/td>\n        <td>\u591a\u4e91<\/td>\n        <td>\u4e1c\u5317\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">68 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-28 \u5468\u56db<\/td>\n        <td style=\"color:#ff5040;\">10\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >0\u00b0<\/td>\n        <td>\u6674<\/td>\n        <td>\u897f\u5317\u98ce3\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">97 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-29 \u5468\u4e94<\/td>\n        <td style=\"color:#ff5040;\">8\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >4\u00b0<\/td>\n        <td>\u6674<\/td>\n        <td>\u4e1c\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">62 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-30 \u5468\u516d<\/td>\n        <td style=\"color:#ff5040;\">13\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >8\u00b0<\/td>\n        <td>\u591a\u4e91~\u9634<\/td>\n        <td>\u4e1c\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-2\">59 \u826f<\/span><\/td>    <\/tr>\n        <tr>\n        <td>2021-01-31 \u5468\u65e5<\/td>\n        <td style=\"color:#ff5040;\">14\u00b0<\/td>\n        <td style=\"color:#3097fd;\" >8\u00b0<\/td>\n        <td>\u9634~\u5c0f\u96e8<\/td>\n        <td>\u4e1c\u5357\u98ce2\u7ea7<\/td>\n        <td><span class=\"history-aqi wea-aqi-1\">34 \u4f18<\/span><\/td>    <\/tr>\n    <\/table>\n"
    
}



```

## JSON格式 data = resp.json()["data"]

网页的返回内容的类型是str类型的，如果它符合JSON格式，则可以使用json( )方法将其转换为字典类型，以方便解析。

```python
resp = requests.get(url, headers=headers, params=params)
data = resp.json()["data"]
print(data)
```

得到数据

```
D:\program\python3.8.10\python.exe D:/python/Python例子/爬取上海10年天气/main.py
<ul class="history-msg">
    <li>平均高温：<em class="orange-txt">22°</em>&nbsp;&nbsp;&nbsp;&nbsp;平均低温：<em class="blue-txt">14°</em></li>
    <li>极端高温：<em class="orange-txt">33°</em><b>(2022-04-12)</b></li>
    <li>极端低温：<em class="blue-txt">7°</em><b>(2022-04-01)</b></li>
        <li>平均空气质量指数：<em class="blod-txt">43</em></li>
    <li>空气最好：<em class="green-txt">15 优</em><b>(04月24日)</b></li>
    <li>空气最差：<em class="yellow-txt">73良</em><b>(04月28日)</b></li>
    </ul>
<table class="history-table" width="100%">
    <tr>
        <th width="169">日期</th>
        <th width="68">最高温</th>
        <th width="68">最低温</th>
        <th width="122">天气</th>
        <th>风力风向</th>
        <th width="140">空气质量指数</th>    </tr>
        <tr>
        <td>2022-04-01 周五</td>
        <td style="color:#ff5040;">14°</td>
        <td style="color:#3097fd;" >7°</td>
        <td>多云~阴</td>
        <td>北风3级</td>
        <td><span class="history-aqi wea-aqi-1">36 优</span></td>    </tr>
        <tr>
        <td>2022-04-02 周六</td>
        <td style="color:#ff5040;">16°</td>
        <td style="color:#3097fd;" >7°</td>
        <td>多云~晴</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-1">37 优</span></td>    </tr>
        <tr>
        <td>2022-04-03 周日</td>
        <td style="color:#ff5040;">15°</td>
        <td style="color:#3097fd;" >8°</td>
        <td>晴</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-1">28 优</span></td>    </tr>
        <tr>
        <td>2022-04-04 周一</td>
        <td style="color:#ff5040;">19°</td>
        <td style="color:#3097fd;" >11°</td>
        <td>多云~阴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">36 优</span></td>    </tr>
        <tr>
        <td>2022-04-05 周二</td>
        <td style="color:#ff5040;">14°</td>
        <td style="color:#3097fd;" >11°</td>
        <td>多云~阴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">45 优</span></td>    </tr>
        <tr>
        <td>2022-04-06 周三</td>
        <td style="color:#ff5040;">25°</td>
        <td style="color:#3097fd;" >13°</td>
        <td>多云</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-2">54 良</span></td>    </tr>
        <tr>
        <td>2022-04-07 周四</td>
        <td style="color:#ff5040;">27°</td>
        <td style="color:#3097fd;" >13°</td>
        <td>多云</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-2">64 良</span></td>    </tr>
        <tr>
        <td>2022-04-08 周五</td>
        <td style="color:#ff5040;">27°</td>
        <td style="color:#3097fd;" >16°</td>
        <td>多云~阴</td>
        <td>东南风3级</td>
        <td><span class="history-aqi wea-aqi-2">58 良</span></td>    </tr>
        <tr>
        <td>2022-04-09 周六</td>
        <td style="color:#ff5040;">28°</td>
        <td style="color:#3097fd;" >16°</td>
        <td>多云</td>
        <td>东南风3级</td>
        <td><span class="history-aqi wea-aqi-2">52 良</span></td>    </tr>
        <tr>
        <td>2022-04-10 周日</td>
        <td style="color:#ff5040;">26°</td>
        <td style="color:#3097fd;" >18°</td>
        <td>多云~阴</td>
        <td>东南风3级</td>
        <td><span class="history-aqi wea-aqi-1">47 优</span></td>    </tr>
        <tr>
        <td>2022-04-11 周一</td>
        <td style="color:#ff5040;">32°</td>
        <td style="color:#3097fd;" >19°</td>
        <td>晴~阴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-2">57 良</span></td>    </tr>
        <tr>
        <td>2022-04-12 周二</td>
        <td style="color:#ff5040;">33°</td>
        <td style="color:#3097fd;" >18°</td>
        <td>多云~小雨</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">50 优</span></td>    </tr>
        <tr>
        <td>2022-04-13 周三</td>
        <td style="color:#ff5040;">16°</td>
        <td style="color:#3097fd;" >14°</td>
        <td>大雨</td>
        <td>东北风3级</td>
        <td><span class="history-aqi wea-aqi-1">24 优</span></td>    </tr>
        <tr>
        <td>2022-04-14 周四</td>
        <td style="color:#ff5040;">15°</td>
        <td style="color:#3097fd;" >12°</td>
        <td>小雨~阴</td>
        <td>北风3级</td>
        <td><span class="history-aqi wea-aqi-1">19 优</span></td>    </tr>
        <tr>
        <td>2022-04-15 周五</td>
        <td style="color:#ff5040;">18°</td>
        <td style="color:#3097fd;" >11°</td>
        <td>多云~阴</td>
        <td>北风3级</td>
        <td><span class="history-aqi wea-aqi-1">29 优</span></td>    </tr>
        <tr>
        <td>2022-04-16 周六</td>
        <td style="color:#ff5040;">18°</td>
        <td style="color:#3097fd;" >11°</td>
        <td>多云</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-2">51 良</span></td>    </tr>
        <tr>
        <td>2022-04-17 周日</td>
        <td style="color:#ff5040;">20°</td>
        <td style="color:#3097fd;" >14°</td>
        <td>多云~阴</td>
        <td>东风2级</td>
        <td><span class="history-aqi wea-aqi-1">39 优</span></td>    </tr>
        <tr>
        <td>2022-04-18 周一</td>
        <td style="color:#ff5040;">20°</td>
        <td style="color:#3097fd;" >13°</td>
        <td>多云</td>
        <td>东南风1级</td>
        <td><span class="history-aqi wea-aqi-1">35 优</span></td>    </tr>
        <tr>
        <td>2022-04-19 周二</td>
        <td style="color:#ff5040;">22°</td>
        <td style="color:#3097fd;" >14°</td>
        <td>多云~晴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-2">56 良</span></td>    </tr>
        <tr>
        <td>2022-04-20 周三</td>
        <td style="color:#ff5040;">24°</td>
        <td style="color:#3097fd;" >16°</td>
        <td>多云~小雨</td>
        <td>东南风3级</td>
        <td><span class="history-aqi wea-aqi-2">63 良</span></td>    </tr>
        <tr>
        <td>2022-04-21 周四</td>
        <td style="color:#ff5040;">26°</td>
        <td style="color:#3097fd;" >17°</td>
        <td>晴</td>
        <td>南风3级</td>
        <td><span class="history-aqi wea-aqi-2">66 良</span></td>    </tr>
        <tr>
        <td>2022-04-22 周五</td>
        <td style="color:#ff5040;">29°</td>
        <td style="color:#3097fd;" >18°</td>
        <td>多云~中雨</td>
        <td>南风2级</td>
        <td><span class="history-aqi wea-aqi-2">62 良</span></td>    </tr>
        <tr>
        <td>2022-04-23 周六</td>
        <td style="color:#ff5040;">20°</td>
        <td style="color:#3097fd;" >16°</td>
        <td>中雨~阴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">32 优</span></td>    </tr>
        <tr>
        <td>2022-04-24 周日</td>
        <td style="color:#ff5040;">22°</td>
        <td style="color:#3097fd;" >18°</td>
        <td>多云~阴</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">15 优</span></td>    </tr>
        <tr>
        <td>2022-04-25 周一</td>
        <td style="color:#ff5040;">27°</td>
        <td style="color:#3097fd;" >20°</td>
        <td>多云~小雨</td>
        <td>东南风3级</td>
        <td><span class="history-aqi wea-aqi-1">30 优</span></td>    </tr>
        <tr>
        <td>2022-04-26 周二</td>
        <td style="color:#ff5040;">22°</td>
        <td style="color:#3097fd;" >15°</td>
        <td>小雨~阴</td>
        <td>西北风3级</td>
        <td><span class="history-aqi wea-aqi-1">25 优</span></td>    </tr>
        <tr>
        <td>2022-04-27 周三</td>
        <td style="color:#ff5040;">22°</td>
        <td style="color:#3097fd;" >15°</td>
        <td>多云~晴</td>
        <td>东北风3级</td>
        <td><span class="history-aqi wea-aqi-2">52 良</span></td>    </tr>
        <tr>
        <td>2022-04-28 周四</td>
        <td style="color:#ff5040;">20°</td>
        <td style="color:#3097fd;" >13°</td>
        <td>多云~中雨</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-2">73 良</span></td>    </tr>
        <tr>
        <td>2022-04-29 周五</td>
        <td style="color:#ff5040;">15°</td>
        <td style="color:#3097fd;" >12°</td>
        <td>多云</td>
        <td>北风3级</td>
        <td><span class="history-aqi wea-aqi-1">26 优</span></td>    </tr>
        <tr>
        <td>2022-04-30 周六</td>
        <td style="color:#ff5040;">17°</td>
        <td style="color:#3097fd;" >13°</td>
        <td>多云~阴</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-1">32 优</span></td>    </tr>
    </table>


Process finished with exit code 0

```

## df = pd.read_html(data)[0]

```python
resp = requests.get(url, headers=headers, params=params)
data = resp.json()["data"]
df = pd.read_html(data)[0]
print(df)
```

得到数据

```txt
D:\program\python3.8.10\python.exe D:/python/Python例子/爬取上海10年天气/main.py
               日期  最高温  最低温     天气   风力风向 空气质量指数
0   2021-01-01 周五   4°  -1°   晴~多云  西北风2级   52 良
1   2021-01-02 周六   7°   1°   晴~多云  东北风2级   69 良
2   2021-01-03 周日  10°   6°      阴  东北风2级   66 良
3   2021-01-04 周一  13°   7°      阴   东风2级   44 优
4   2021-01-05 周二   8°   2°   阴~多云  东北风3级   49 优
5   2021-01-06 周三   5°  -4°      阴   北风3级   46 优
6   2021-01-07 周四  -3°  -6°      阴  西北风4级   67 良
7   2021-01-08 周五  -1°  -5°    阴~晴  西北风3级   50 优
8   2021-01-09 周六   3°  -1°   晴~多云  西北风3级   57 良
9   2021-01-10 周日   5°  -1°   阴~多云  西北风2级   73 良
10  2021-01-11 周一   6°  -1°   多云~晴  西北风2级   70 良
11  2021-01-12 周二   8°   1°      晴  西南风2级   94 良
12  2021-01-13 周三  14°   4°      晴  西南风2级   80 良
13  2021-01-14 周四  16°   6°   多云~晴   南风2级   80 良
14  2021-01-15 周五  19°   2°    晴~阴  西北风3级   80 良
15  2021-01-16 周六   7°   0°   阴~多云  东北风3级   73 良
16  2021-01-17 周日   5°  -1°    阴~晴  西北风微风   62 良
17  2021-01-18 周一  11°   2°      晴  西南风2级   84 良
18  2021-01-19 周二  11°   6°   多云~晴  东南风3级   68 良
19  2021-01-20 周三  13°  12°   多云~阴  东南风3级   34 优
20  2021-01-21 周四  17°   9°   阴~小雨  东南风2级   46 优
21  2021-01-22 周五  11°   7°     小雨  东北风2级   64 良
22  2021-01-23 周六   8°   4°   小雨~阴   北风3级   61 良
23  2021-01-24 周日  10°   7°      阴  东北风2级   84 良
24  2021-01-25 周一  15°   9°   阴~小雨   东风2级   36 优
25  2021-01-26 周二  10°   6°  小雨~多云  西北风2级   43 优
26  2021-01-27 周三  10°   4°     多云  东北风2级   68 良
27  2021-01-28 周四  10°   0°      晴  西北风3级   97 良
28  2021-01-29 周五   8°   4°      晴   东风2级   62 良
29  2021-01-30 周六  13°   8°   多云~阴  东南风2级   59 良
30  2021-01-31 周日  14°   8°   阴~小雨  东南风2级   34 优

Process finished with exit code 0

```

