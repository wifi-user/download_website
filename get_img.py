#!/usr/bin/env python
import os
import requests
from bs4 import BeautifulSoup
import shutil
import re
import urllib.parse 
# 设置请求头
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# 判断存储文件夹是否存在目录路径 
directory = 'project' 
if directory in os.listdir(): 
    print('project已存在，继续执行') 
else: 
    os.mkdir(directory)
# 遍历所有HTML文件
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        # 读取HTML文件
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 解析HTML内容
        soup = BeautifulSoup(content, 'html.parser')

        # 遍历所有img标签
        imgs = soup.find_all('img')
        print(imgs)
        for img in imgs:
            # 获取图片URL
            img_url = img.get('src')
            if 'http' not in img_url:
                continue
            if img_url is not None:
                # url编码
                #img_url = urllib.parse.unquote(img_url)
                # 匹配以http开头、以.com结尾的URL链接
                pattern = r'http\S+com/'
                # 用空字符串替换匹配到的URL链接
                img_path = re.sub(pattern, '',img_url)

                # 创建保存路径
                print('图片url：',img_url)
                print('存储path：',img_path)
                #img_path = os.path.join(directory, img_url)  # 去除"http开头.com结尾"
                img_dir = os.path.dirname(img_path)
                os.makedirs(img_dir, exist_ok=True)

                # 下载图片
                response = requests.get(img_url)
                print(response)
                with open(img_path, 'wb') as f:
                    shutil.copyfileobj(response.raw, f)
                    print(img_path,'完')
                del response
