import json
import requests
from time import sleep
from datetime import datetime, timedelta, timezone

# 都道府県の単位を合わせる用 東京 => 東京都
t = ["東京"]
f = ["大阪", "京都"]
k = [
    "青森", "岩手", "宮城", "秋田", "山形", "福島",
    "茨城", "栃木", "群馬", "埼玉", "千葉", "神奈川",
    "新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜",
    "静岡", "愛知", "三重", "滋賀", "兵庫", "奈良", "和歌山",
    "鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川",
    "愛媛", "高知", "福岡", "佐賀", "長崎", "熊本", "大分",
    "宮崎", "鹿児島", "沖縄"
]

# ファイル名
file_path = "data/prefectures.json"


# アップデート時間
jst = timezone(timedelta(hours=+9), "JST")
now = datetime.now(jst).strftime("%Y-%m-%d %H:%M")

# API
n = datetime.now(timezone(timedelta(hours=+10), "JST")).hour
base_url = {"prefectures_data": "https://covid19-japan-web-api.now.sh/api/v1/prefectures",
            "before_prefectures_data": "https://raw.githubusercontent.com/miya/covid19-jp-api/{}/before_prefectures.json".format(n)}

# 公開用json
json_dic = {
    "update": now,
    "data_source": base_url["prefectures_data"],
    "prefectures_data": {},
    "total_nums": {
        "total_cases": 0,
        "total_deaths": 0
    },
    "before_prefectures_data": {},
    "before_total_nums": {
        "total_cases": 0,
        "total_deaths": 0
    }
}

def create_json(json_type):
    data = {}
    get_json_dic = {}
    total_cases = 0
    total_deaths = 0
    cnt = 0

    for i in range(5):
        r = requests.get(base_url[json_type])
        s = r.status_code
        if s == 200:
            get_json_dic = r.json()
            break
        else:
            cnt += 1
            sleep(1)
        if cnt >= 4:
            print("データを取得できませんでした。")
            exit()

    for i in get_json_dic:

        # 都道府県名の単位の修正
        name_ja = i["name_ja"]
        if name_ja in t:
            i["name_ja"] = name_ja + "都"
        elif name_ja in f:
            i["name_ja"] = name_ja + "府"
        elif name_ja in k:
            i["name_ja"] = name_ja + "県"

        # 各都道府県の感染者数・死亡者数を加算
        total_cases += i["cases"]
        total_deaths += i["deaths"]

        # 都道府県名、感染者数、死亡者数を格納
        data.update({
            i["name_ja"]: {
                "cases": i["cases"],
                "deaths": i["deaths"]
            }
        })

    # 公開用jsonにデータを格納
    if json_type == "prefectures_data":
        nums_type = "total_nums"
    else:
        nums_type = "before_total_nums"
    json_dic.update({
        json_type: data,
        nums_type: {
            "total_cases": total_cases,
            "total_deaths": total_deaths
        }
    })


if __name__ == "__main__":
    for i in base_url:
        print(base_url[i])
        create_json(i)

    # jsonファイルの生成
    with open(file_path, "w") as file_:
        json.dump(json_dic, file_, ensure_ascii=False, indent=2)
