#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 判断存储文件夹是否存在目录路径
directory = './project'
if directory in os.listdir():
    print('project已存在，继续执行')
# 发送 GET 请求获取网页内容
url = 'https://redbu1l.github.io/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到 lu 标签 class 值为 nav 下的所有 a 标签
lu_nav = soup.find('ul', {'id': 'mysidebar'})
a_tags = lu_nav.find_all('a')

# 遍历所有 a 标签
for a_tag in a_tags:
    link = a_tag['href']
    # 如果链接的 href 属性值以 "#" 开头，跳过不处理
    if link.startswith('#'):
        continue
    # 将链接补全
    if link.startswith('http'):
        file_url = link
    else:
        file_url = url + link

    # 获取文件名
    filename = link.split('/')[-1]
    if filename == '':
        filename = 'index.html'
    if not filename.endswith('.html'):
        filename += '.html'

    # 发送 GET 请求获取文件内容
    response = requests.get(file_url, headers=headers)

    # 解析文件内容，将 script 标签内容删除
    file_soup = BeautifulSoup(response.text, 'html.parser')
    for script in file_soup.find_all('script'):
        script.decompose()

    # 保存文件到本地
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(str(file_soup))
    print(f'{filename} saved.')
