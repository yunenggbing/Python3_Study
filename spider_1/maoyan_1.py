import requests

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36'}
for i in range(10):
    url = 'https://maoyan.com/board/4?offset=' + str(i * 10)

    items = []

    html = requests.get(url, headers=headers)

    html.encoding = 'utf-8'

    bs = BeautifulSoup(html.text, 'lxml')

    class1 = bs.find_all('dd')

    print(class1)

    items.extend(class1)
    for item in items:
        file = {}
        file['index'] = item.i.string
        file['name'] = item.a.attrs['title']
        file['date'] = item.find(name='p', attrs={'class': 'releasetime'}).string.strip()
        with  open('file.txt', 'a', encoding='utf-8') as  f:
            f.write(str(file) + '\n')
            f.close()
