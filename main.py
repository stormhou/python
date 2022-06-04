
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

    pd.concat(df_list).to_excel("上海2011年-2021年天气数据1.xlsx", index=False)


if __name__ == '__main__':
    main()