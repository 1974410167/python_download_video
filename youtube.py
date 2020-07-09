# coding = utf-8

import os
import datetime
import sys
import you_get
import threading
import youtube_dl
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree


def read_url():

    with open("C://Users//19744//Desktop//urls.txt") as f:
        url_list = f.readlines()
    return url_list


def folder_name():

    time = datetime.datetime.now()
    t = str(time.year)+'.'+str(time.month)+'.'+str(time.day)
    return t

def download_path():

    folder = folder_name()

    absolute_path = "D://video_res//" + folder+"//"

    if os.path.exists(absolute_path) is False:
        os.mkdir(absolute_path)

    return absolute_path

def you_get_download(url,path):

    os.system(f'you-get -o {path} {url}')
    # sys.argv = ['you-get','-o',path,url]
    # you_get.main()

def youtube_dl_download(url,path):

    ydl_opts = {
        'outtmpl':path+'%(title)s.%(ext)s',
        'writesubtitles': True,
        'subtitleslangs':['zh-Hans','en'],
        'writeautomaticsub': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as f:
        result = f.download(url)
        print(result)

def main(url,path):

    url_list = [url]
    youtube_dl_download(url_list, path)

def url_message(url):

    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': '*/*',
        'Cookie': 'VISITOR_INFO1_LIVE=bl4jG0T-Fc0; YSC=OK4FSA8JCkM; PREF=; GPS=1; ST-17pm9r8=itct=CBMQtSwYACITCJLFq9HPruoCFYEzYAoduuQDdzIJZy1jaGFubmVs&csn=Kdr9XsnZOYLngAO1gK-4DQ',
    }

    try:
        r = requests.get(url, headers)
        t = etree.HTML(r.text)
        xpath1 = "//meta[@property='og:title']/@content"
        xpath2 = "//meta[@property='og:description']/@content"
        result1 = t.xpath(xpath1)
        result2 = t.xpath(xpath2)
        file_name = result1[0]
        if len(file_name)>10:
            file_name = file_name[:10]

        url_message_dict = {}
        url_message_dict['url'] = url
        url_message_dict['filename'] = file_name
        url_message_dict['title'] = result1[0]
        url_message_dict['description'] = result2[0]
        return url_message_dict
    except:
        print('url_message请求失败！')
        return {}


def write_url_message(dict,path):

    url = dict.get('url','通用url')
    filename = dict.get('filename','通用文件名')
    title = dict.get('title','通用标题')
    description = dict.get('description','通用描述')

    file_name = filename.replace(" ","B").replace("?",'B').replace(":",'B').replace("/","B").replace("&",'B').replace('<','B').replace('>','B').replace('|','b').replace('"','B')

    file_path = path+file_name+'//'

    if os.path.exists(file_path) is False:
        os.mkdir(file_path)

    with open(file_path+file_name+'.txt', 'w', encoding='utf-8') as f:
        f.write('url: ' + url + '\n')
        f.write('title: ' + title + '\n')
        f.write('description: ' + description + '\n')

    return file_path


if __name__ == '__main__':

    url_list = read_url()

    path = download_path()


    with ThreadPoolExecutor(max_workers=5) as f:
        for url in url_list:

            dict = url_message(url)

            file_path = write_url_message(dict, path)

            try:
                result = f.submit(main,url,file_path)
            except:
                # result = f.submit(you_get_download,url,file_path)
                print(f'{url}s失败')





