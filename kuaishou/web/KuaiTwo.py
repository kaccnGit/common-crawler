# -*- coding: utf-8 -*-
"""
# @Time    : 2021-01-05 15:37
# @Author  : wangkangxi
# @File    : KuaiTwo.py
"""
import requests, json, re, time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    "Cookie": "kuaishou.live.bfb1s=9b8f70844293bed778aade6e0a8f9942; clientid=3; did=web_a9d0c104cbfd24374a5dad685b26dd70; client_key=65890b29; didv=1594279985370; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594622985; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1594885138; userId=127345174; userId=127345174; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAVwApsvd6d5LEq37Xwy4gVgfinmYKMKK5hT0t2Dl7nctTR46oTuc1Ku530mlTABB5PbNPqsDF4m5GjgTeFBbDgi4xBQ3cXCQHWfg-T7b9259MfvgaMoKB-r4R92eUR3VgXQz8bK7cJDrX_zKVEhh3WZscoFagE2xXXmFB9nXlmXMei2w5TAQih60pOlFpVMgqakLULnxvPY-BFIlNyoUlU8aEgCrAu8bFEUPixNgRvVq1Nb0ZSIglCraqHTuUQ_z3VWWktXq5nxr2SJYhM3aujbIbG9pAj0oBTAB; kuaishou.live.web_ph=3e0f6f0394323c61795f3382dabebad6f407"}

def get_page1():
    response = requests.get(url="https://live.kuaishou.com/profile/TXXW-666666", headers=headers)
    res = response.text
    print(res)
    video_page1 = re.findall('"id":"VideoFeed:(.*?)"',res)
    print(video_page1)


def get_video(resp):
    eid = re.findall('"id":"(.*?)"',resp)
    id = []
    count = 0
    while len(eid)>count:

        id.append(eid[count])
        count=count+2

    print(id)
    return id


def get_page(pcursor):
    json0 = {
        "operationName": "publicFeedsQuery",
        "variables": {
            "principalId": "TXXW-666666",
            "pcursor": pcursor,
            "count": 24
        },
        "query": "query publicFeedsQuery($principalId: String, $pcursor: String, $count: Int) {  publicFeeds(principalId: $principalId, pcursor: $pcursor, count: $count) {    pcursor    live {      user {        id        avatar        name        __typename      }      watchingCount      poster      coverUrl      caption      id      playUrls {        quality        url        __typename      }      quality      gameInfo {        category        name        pubgSurvival        type        kingHero        __typename      }      hasRedPack      liveGuess      expTag      __typename    }    list {      id      thumbnailUrl      poster      workType      type      useVideoPlayer      imgUrls      imgSizes      magicFace      musicName      caption      location      liked      onlyFollowerCanComment      relativeHeight      timestamp      width      height      counts {        displayView        displayLike        displayComment        __typename      }      user {        id        eid        name        avatar        __typename      }      expTag      __typename    }    __typename  }}"
    }

    resp = requests.post(url="https://live.kuaishou.com/m_graphql",headers=headers,json=json0).text
    resp_page = json.loads(resp)["data"]["publicFeeds"]["pcursor"]
    # print(resp)
    # li = json.loads(resp)["data"]["publicFeeds"]["list"]
    # print(li)


    id = get_video(resp)
    uri_list = video_address(id)

    video_detial(uri_list)

    return get_page(resp_page)


def video_address(id):
    url_list = []
    for i in range(len(id)):
        url_list.append("https://live.kuaishou.com/u/TXXW-666666/"+id[i]+"?did=web_a9d0c104cbfd24374a5dad685b26dd70")

    return url_list


def video_detial(uri_list):
    for i in range(len(uri_list)):
        uri = uri_list[i]

        response = requests.get(url=uri,headers=headers).text
        # time.sleep(0.5)
        try:
            # 标题
            title = re.findall('"caption":"(.*?)"',response)[0]
            # 播放量
            playback = re.findall('"displayView":"(.*?)"',response)[0]
            # 点赞数
            playlike = re.findall('"displayLike":"(.*?)"',response)[0]
            print(uri,title,playback,playlike)
        except Exception as e:
            print(uri,"暂无数据")


if __name__ == '__main__':
    # get_page("")
    get_page1()
