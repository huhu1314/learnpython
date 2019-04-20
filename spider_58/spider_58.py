# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


#58同城的二手市场主页面
start_url = 'https://sz.58.com/sale.shtml'
url_host = 'https://sz.58.com/'
#定义一个爬虫函数来获取二手市场页面中的全部大类页面的连接
def get_channel_urls(url):
    #使用Requests库来进行一次请求
    web_data = requests.get(url)
    #使用BeautifulSoup对获取到的页面进行解析
    soup = BeautifulSoup(web_data.text, 'lxml')
    #根据页面内的定位信息获取到全部大类所对应的连接
    urls = soup.select('ul.ym-submnu > li > b > a')
    #作这两行处理是因为有的标签有链接，但是却是空内容
    for link in urls:
        if link.text.isspace():
            continue
        else:
            page_url = url_host + link.get('href')
            print(page_url)

if __name__ == '__main__':
    get_channel_urls(start_url)