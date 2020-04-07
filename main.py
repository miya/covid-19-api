import json
import requests

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

base_url = "https://covid19-japan-web-api.now.sh/api/v1/prefectures"
r = requests.get(base_url)

json_dic = {}

get_json_dic = r.json()
for i in get_json_dic:

    name_ja = i["name_ja"]
    if name_ja in t:
        i["name_ja"] = name_ja + "都"
    elif name_ja in f:
        i["name_ja"] = name_ja + "府"
    elif name_ja in k:
        i["name_ja"] = name_ja + "県"

    json_dic.update({
        i["name_ja"]: {
            "cases": i["cases"],
            "deaths": i["deaths"]
        }
    })

with open("data/prefectures.json", "w") as f:
    json.dump(json_dic, f, ensure_ascii=False, indent=2)
