import requests
import random
from lxml import etree
import re
import json
import os
import datetime

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
]

headers = {
    'User-Agent':random.choice(user_agent_list),
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Cookie':'SLARDAR_WEB_ID=9d5842f4-27dd-4392-8626-ce8e03887e17; sso_auth_status=2730bde7fda9021a0e6ef36c43cd0a1b; sso_uid_tt=0413ac6f61a4b21974d9c7ff5800856d; sso_uid_tt_ss=0413ac6f61a4b21974d9c7ff5800856d; toutiao_sso_user=5d03f1a42f53f21a765afdd2eb053ee1; toutiao_sso_user_ss=5d03f1a42f53f21a765afdd2eb053ee1; passport_auth_status=c63c6d0ee84596e3f98186fd5a9359ae%2Ca7737c13552b64608101405adce1008e; sid_guard=b406ab75f49b568f108317a7358005b8%7C1593770282%7C5184000%7CTue%2C+01-Sep-2020+09%3A58%3A02+GMT; uid_tt=de6a38e512b4bfa245ddb58245b0e714; uid_tt_ss=de6a38e512b4bfa245ddb58245b0e714; sid_tt=b406ab75f49b568f108317a7358005b8; sessionid=b406ab75f49b568f108317a7358005b8; sessionid_ss=b406ab75f49b568f108317a7358005b8; _ga=GA1.2.1822623887.1593788578; _gid=GA1.2.694349201.1593788578; tt_webid=6845973972434830862; passport_csrf_token=a0e6fa53d6f5a9948ac12806b772db73; _gat=1'
}


def read_url():

    with open("C://Users//19744//Desktop//pipi.txt") as f:
        url_list = f.readlines()

    return url_list

def redirect_url():

    url_list = read_url()
    for url in url_list:

        url = url.strip()
        r = requests.get(url,headers=headers)
        # 得到重定向url

        t = r.url
        com = re.compile('\d{19}')
        s = com.findall(t)
        ar = s[0]

        base_url = 'https://h5.pipix.com/bds/webapi/item/detail/?item_id='+ar+'&source=share'
        print(base_url)
        r1 = requests.get(base_url,headers=headers)
        r1.encoding='utf-8'
        js = r1.json()
        item_id = js['data']['item']['video']['video_high']['url_list'][0]['url']

        item_id = item_id.split('?')
        true_url = item_id[0]

        r2 = requests.get(true_url)

        filename = ar

        path = download_path()+filename
        with open(path+'.mp4','wb') as f:
            f.write(r2.content)

def download_path():

    folder = folder_name()

    absolute_path = "D://pipixia//" + folder+"//"

    if os.path.exists(absolute_path) is False:
        os.mkdir(absolute_path)

    return absolute_path

def folder_name():

    time = datetime.datetime.now()
    t = str(time.year)+'.'+str(time.month)+'.'+str(time.day)

    return t

redirect_url()