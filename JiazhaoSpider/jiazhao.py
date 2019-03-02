import requests
from lxml import etree
import os
html = requests.get('https://www.jiazhao.com/jinggaobiaozhi/')
html = etree.HTML(html.content)
result_href = html.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a/@href')
titleList = html.xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a/@title")
# 创建文件夹
path = os.getcwd() #获取当前路径
file_path = path +"\图片文件" #图片文件夹
file_path_name = path +"\图片名称" #图片名称文件夹
file_path_miaoshu = path +"\图片详情" #图片详细说明文件夹
if not os.path.exists(file_path):
    os.mkdir(file_path)
if not os.path.exists(file_path_name):
    os.mkdir(file_path_name)
if not os.path.exists(file_path_miaoshu):
    os.mkdir(file_path_miaoshu)
n = 1
for i in result_href:
    url = 'https://www.jiazhao.com/jinggaobiaozhi' + i[-5:]
    p_html = requests.get(url)
    m_html = etree.HTML(p_html.content)
    #提取图片链接
    jpgLink = m_html.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/p/img/@src')[0]
    p_url = 'http:' + jpgLink  #拼接链接
    # 提取图片标题
    p_titl = m_html.xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/p/img/@alt")[0]
    #提取图片详细信息
    miaoshu = m_html.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/h2/text()')
    miaoshu_1 = ''.join(miaoshu)
    filename = '%s/%s.jpg' % (file_path, n)
    file_name = '%s/%s.txt' % (file_path_name, n)
    file_miaoshu = '%s/%s.txt' % (file_path_miaoshu, n)
    print(p_url, p_titl)
    with open(filename, "wb+") as jpg:
        jpg.write(requests.get(p_url).content)
    with open(file_name, "w") as jpg:
        jpg.write(p_titl)
    with open(file_miaoshu, "w") as jpg:
        jpg.write(miaoshu_1)
    n += 1


