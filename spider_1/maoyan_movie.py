# -*- coding：utf-8 -*-

# 爬取猫眼排名100的电影名称

import time

import chardet
import requests
import re
import json
from requests.exceptions import RequestException


def get_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/84.0.4147.105 Safari/537.36'}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            # res.encoding = 'utf-8'
            res.encoding = chardet.detect(res.content)['encoding']

            return res.text
        return None
    except RequestException:
        return None


def get_content(page):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, page)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_file(content):
    with  open('maoyan.txt', 'a', encoding='utf-8')  as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        print('----开始写入文件---')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    for item in get_content(html):
        print(item)
        write_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
