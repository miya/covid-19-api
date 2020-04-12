import json
import requests
from time import sleep

# API
base_url = "https://covid19-japan-web-api.now.sh/api/v1/prefectures"

# ファイル名
file_path = "data/before_prefectures.json"


def create_json():
    cnt = 0
    get_json_dic = {}

    for i in range(5):
        r = requests.get(base_url)
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

    with open(file_path, "w") as file_:
        json.dump(get_json_dic, file_, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    create_json()
