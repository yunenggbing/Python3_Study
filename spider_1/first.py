# -*- coding：utf-8 -*-
# no.1 员工奖金
# from pip._vendor.distlib.compat import raw_input
# 方法一
# i = int(raw_input('净利润：'))
# r = 0
# if i <= 100000:
#     m = m + i * 0.1
# elif 100000 < i <= 200000:
#     m = (i - 100000) * (7.5 / 100) + 100000 * (10 / 100)
# elif 200000 < i <= 400000:
#     m = 100000 * (0.1 + 0.075) + (i - 200000) * 0.05
# elif 400000 < i <= 600000:
#     m = 100000 * (0.1 + 0.075) + 200000 * 0.05 + (i - 400000) * 0.03
# elif 600000 <= i <= 1000000:
#     m = 100000 * (0.1 + 0.075) + 200000 * (0.05 + 0.03) + (i - 600000) * 0.015
# else:
#     m = 100000 * (0.1 + 0.075) + 200000 * (0.05 + 0.03) + 400000 * 0.015 + (i - 1000000) * 0.01
# print(m)

# 方法二
# i = int(raw_input('净利润：'))
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print((i - arr[idx]) * rat[idx])
#         i = arr[idx]
#
# print(r)

# no.2 求未知整数

# 程序分析：
#
# 1、则：x + 100 = n2, x + 100 + 168 = m2
#
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
#
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
#
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
#
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
#
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
#
# 7、接下来将 i 的所有数字循环计算即可。
# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# try:
#     f = open(r'D:\Users\yunengbing\Desktop\2.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# import requests  # 导入requests包
# from bs4 import BeautifulSoup
#
# url = 'http://www.cntour.cn/'
# str1 = requests.get(url)
# soup = BeautifulSoup(str1.text, 'lxml')
# data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
#
# for item in data:
#     res = {
#         'title': item.get_text(),
#         'link':item.get('href')
#     }
# print(data)
# print(res)

import requests

import time
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    str1 = requests.get(target)
    str1.encoding = 'utf-8'
    res = str1.text
    bs = BeautifulSoup(res, 'lxml')
    res1 = bs.find('div', id='content')
    content1 = res1.text.strip().split('\xa0' * 4)
    return content1


if __name__ == '__main__':
    num='8549128'
    for num in range(8549128,8568034,1):
        num1=str(num)
        url='https://www.xsbiquge.com/15_15338/'+num1+'.html'
        print(url)
        book_name = '诡秘之主.txt'
        str1 = requests.get(url)
        str1.encoding = 'utf-8'
        res = str1.text
        bs = BeautifulSoup(res, 'lxml')
        print(bs.text)
        res1 = bs.find('div', id='content')
        name1=bs.find('a')
        name=name1.get('h1')
        content1 = res1.text.strip().split('\xa0'*4)
        with open(book_name, 'a', encoding='utf-8') as f:
              f.write(name1.string)
              f.write('\n')
              f.write('\n'.join(content1))
              f.write('\n')



