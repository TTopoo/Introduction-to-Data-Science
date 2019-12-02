# -*-coding:utf8-*-
# https://bangumi.bilibili.com/view/web_api/season?season_id=28004
# https://api.bilibili.com/pgc/view/web/media?media_id=28221401
# https://blog.csdn.net/weixin_38208912/article/details/88937334
import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload
import traceback
from multiprocessing.dummy import Pool as ThreadPool


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time():
        return int(round(time.time() * 1000))

    return current_milli_time()


reload(sys)


def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


uas = LoadUserAgents(r"user_agents.txt")
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/23058758',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
heads = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Host': 'api.bilibili.com',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
# Please replace your own proxies.
proxies = {
    'http': 'http://111.29.3.187:8080',

}
time1 = time.time()

urls = []

# Please change the range data by yourself.
for i in range(15009132, 16000000):  # 用户id的范围
    url = 'https://space.bilibili.com/' + str(i)
    urls.append(url)


    def getsource(url):
        payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
            'mid': url.replace('https://space.bilibili.com/', '')
        }
        ua = random.choice(uas)  # 序列中随机选择一个浏览器信息
        head = {
            'User-Agent': ua,
            'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(
                random.randint(10000, 100000))
        }
        try:
            jscontent = requests.session().post('http://space.bilibili.com/ajax/member/GetInfo',
                                                headers=head,
                                                data=payload,
                                                proxies=proxies,
                                                ).text
        except Exception as e:
            print(e)
            pass

        time2 = time.time()
        try:
            jsDict = json.loads(jscontent)
            # print(jsDict)
            statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
            if statusJson == True:
                if 'data' in jsDict.keys():
                    jsData = jsDict['data']
                    mid = jsData['mid']
                    name = jsData['name']
                    sex = jsData['sex']
                    rank = jsData['rank']
                    face = jsData['face']
                    regtimestamp = jsData['regtime']
                    regtime_local = time.localtime(regtimestamp)
                    regtime = time.strftime("%Y-%m-%d %H:%M:%S", regtime_local)
                    spacesta = jsData['spacesta']
                    birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'  # 生日
                    sign = jsData['sign']
                    level = jsData['level_info']['current_level']
                    OfficialVerifyType = jsData['official_verify']['type']
                    OfficialVerifyDesc = jsData['official_verify']['desc']
                    OfficialVerifyType = jsData['official_verify']['suffix']
                    vipType = jsData['vip']['vipType']
                    vipStatus = jsData['vip']['vipStatus']
                    toutu = jsData['toutu']
                    toutuId = jsData['toutuId']
                    coins = jsData['coins']
                    bagde = jsData['fans_badge']
                    print("Succeed get user info: " + str(mid) + "\t" + str(time2 - time1))
                    try:
                        heads = {
                            'User-Agent': ua,
                        }
                        res = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str(mid) + '&jsonp=jsonp',
                                           headers=heads,
                                           proxies=proxies,
                                           )
                        viewinfo = requests.get(
                            'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp', 
                            headers=heads,
                            proxies=proxies,
                            )
                        print(res.status_code ,viewinfo.status_code)
                        js_fans_data = json.loads(res.text)
                        js_viewdata = json.loads(viewinfo.text)
                        following = js_fans_data['data']['following']  # 关注
                        fans = js_fans_data['data']['follower']  # 粉丝
                        archiveview = js_viewdata['data']['archive']['view']  # 播放数
                        article = js_viewdata['data']['article']['view']  # 阅读数
                        try:
                            bangres = requests.get(
                                'https://api.bilibili.com/x/space/bangumi/follow/list?type=1&follow_status=0&pn=1&ps=50&vmid=' + str(
                                    mid),
                                headers=heads,
                                proxies=proxies,
                                )
                            bres = json.loads(bangres.text)
                            bnum = bres['data']['total']  # 总订阅番剧
                            # blist = bres['data']['list']  # 订阅番剧列表
                            '''
                            if bnum > 50:
                                for i in range(0, bnum // 50):
                                    bangres = requests.get(
                                        'https://api.bilibili.com/x/space/bangumi/follow/list?type=1&follow_status=0&pn=' + str(
                                            i + 2) + '&ps=50&vmid=' + str(
                                            23058758), headers=heads)
                                    bres = json.loads(bangres.text)
                                    blist = blist + bres['data']['list']
                            '''
                        except:
                            bnum = 0
                    except:
                        following = 0
                        fans = 0
                        archiveview = 0
                        article = 0
                else:
                    print('no data now')
                try:
                    # Please write your MySQL's information.
                    conn = pymysql.connect(
                        host='localhost', user='root', passwd='ruru9999', db='bilibili', charset='utf8')
                    cur = conn.cursor()
                    cur.execute(
                        'INSERT INTO bilibili_user_info(mid, name, sex, t_rank, face, regtime, spacesta, birthday, sign, level, \
                                OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                                toutu, toutuId, coins, following, fans ,archiveview, article, bnum) \
                    VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                            "%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s","%s")'
                        %
                        (mid, name, sex, rank, face, regtime, spacesta, \
                         birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                         toutu, toutuId, coins, following, fans, archiveview, article, bnum))
                    conn.commit()
                except Exception as e:
                    print(e)
            else:
                print("Error: " + url)
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    pool = ThreadPool(1)
    try:
        results = pool.map(getsource, urls)
    except Exception as e:
        print(e)

    pool.close()
    pool.join()
