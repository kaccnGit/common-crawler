# -*- coding: utf-8 -*-
"""
# @Time    : 2021-01-05 20:00
# @Author  : wangkangxi
# @File    : KuaiSearch.py
"""
import requests, json, re, time

headers = {
    "Host": "video.kuaishou.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://video.kuaishou.com",
    # "Cookie": ""}
    # "Cookie": "did=web_a7914eac2bfa47efbbc1e885dce8c0c3; didv=1609816057000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1609827084; userId=2195021671; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjcyODg3NDEzLjE2MDk4Mzg1ODEzODAuMjAyNQ==|MS43NjQ1ODM2OTgyODY2OTgyLjY1NzUxNDkxLjE2MDk4Mzg1ODEzODAuMjAyNg==|0|graphql-server|webservice|false|NA; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB8vzPCgrjqAT7sRwu99fQkEHbqn6Tp8-UYrHo_yqm9mba3fqWwEuU8Udi27hSm3aFVJeMzkYpks1qgLF16BexhnkBwCspJysjbsry-ZunLrLcSO9fZgsIAfocInZ5oJQOYfa8v6I5vFGQIPgUHeR5NAK9guLlKyCVHjeDe70R_1GfKL7H2j5VecYAIeha8SljWkMxYNbDwzWGC5GW-u-_nhoSg3ZkWJHNsQvvc8vsvUksYr6BIiAhfXY70Edrf9hWvatCAhhuNuZB94r2SYds6q8W0xUxpygFMAE; kuaishou.server.web_ph=59943bd5bb9eeb348421e66eec939a144963"}
    "Cookie":
              # "did=web_a7914eac2bfa47efbbc1e885dce8c0c3; "
              # "didv=1609816057000; "
              # "kpf=PC_WEB; "
              # "kpn=KUAISHOU_VISION; "
              # "clientid=3; "
              # "client_key=65890b29; "
              # "Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1609827084; "
              "userId=2195021671; "
              "kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB8vzPCgrjqAT7sRwu99fQkEHbqn6Tp8-UYrHo_yqm9mba3fqWwEuU8Udi27hSm3aFVJeMzkYpks1qgLF16BexhnkBwCspJysjbsry-ZunLrLcSO9fZgsIAfocInZ5oJQOYfa8v6I5vFGQIPgUHeR5NAK9guLlKyCVHjeDe70R_1GfKL7H2j5VecYAIeha8SljWkMxYNbDwzWGC5GW-u-_nhoSg3ZkWJHNsQvvc8vsvUksYr6BIiAhfXY70Edrf9hWvatCAhhuNuZB94r2SYds6q8W0xUxpygFMAE"}


def get_video_list():
    json0 = {
        "operationName": "visionSearchPhoto",
        "variables": {
            "keyword": "天使熊",
            "pcursor": "1",
            "page": "searchPhoto",
            "searchSessionId": "MTRfMjE5NTAyMTY3MV8xNjA5ODQ4OTU1ODQ1X-e9keaYk-S6kV8yMzYx"
        },
        "query": "query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page) {\n    result\n    llsid\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    resp = requests.post(url="https://video.kuaishou.com/graphql", headers=headers, json=json0).text
    return resp


if __name__ == '__main__':
    print(get_video_list())
