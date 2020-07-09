import re
import os
import datetime
import requests

def read_url():
    with open("C://Users//19744//Desktop//douyin.txt") as f:
        url_list = f.readlines()
    return url_list

def download_path():
    folder = folder_name()
    absolute_path = "D://douyin//" + folder+"//"
    if os.path.exists(absolute_path) is False:
        os.mkdir(absolute_path)
    return absolute_path

def folder_name():
    time = datetime.datetime.now()
    t = str(time.year)+'.'+str(time.month)+'.'+str(time.day)
    return t

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
}

def main(url):

    r = requests.get(url,headers=headers)
    url_1 = r.url
    com = re.compile('\d{19}')
    s = com.findall(url_1)
    item_id = s[0]

    get_ture_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+item_id+'&dytk='

    r1 = requests.get(get_ture_url,headers=headers)
    r1.encoding = 'utf-8'

    json = r1.json()

    base_url = json['item_list'][0]['video']['play_addr']['url_list'][0]


    tt = base_url.replace('playwm','play')

    filename = item_id
    r2 = requests.get(tt,headers=headers)
    print(f'{tt}下载成功！')
    path = download_path() + filename
    with open(path + '.mp4', 'wb') as f:
        f.write(r2.content)

if __name__ == '__main__':

    url_list = read_url()
    for url in url_list:
        url = url.strip()
        main(url)

