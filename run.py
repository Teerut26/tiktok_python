from TikTokApi import TikTokApi
import json
from ClassTiktok import ClassTiktokfromdict
from datetime import datetime
import time
import requests
from modules.Colors import bcolors


def formattime(ts):
    return time.strftime("%D %H:%M", time.localtime(int(ts)))


def downloadFile(url, path):
    res = requests.get(url)
    f = open(path, "wb").write(res.content)


def run():
    api = TikTokApi.get_instance()
    results = int(input("limit : "))
    trending = api.by_trending(count=results, custom_verifyFp="")

    for x in trending:
        downloadFile
        print(f"{bcolors.OKGREEN}Video ID{bcolors.ENDC} : {x['id']}")
        print(f"{bcolors.OKGREEN}CreateTime{bcolors.ENDC} : {formattime(x['createTime'])}")
        print(f"{bcolors.OKGREEN}Author{bcolors.ENDC} : {x['author']['uniqueId']}")
        print(f"{bcolors.OKGREEN}Music{bcolors.ENDC} : {x['music']['title']}")
        print(f"{bcolors.OKGREEN}DiggCount{bcolors.ENDC} : {x['stats']['diggCount']:,}")
        print(f"{bcolors.OKGREEN}ShareCount{bcolors.ENDC} : {x['stats']['shareCount']:,}")
        print(f"{bcolors.OKGREEN}PlayCount{bcolors.ENDC} : {x['stats']['playCount']:,}")
        print(f"{bcolors.OKGREEN}Video Ratio{bcolors.ENDC} : {x['video']['ratio']}")
        print(f"=========================================")
        # downloadFile(x['video']['downloadAddr'], f"video/{str(x['id'])}.mp4")


if __name__ == "__main__":
    run()
