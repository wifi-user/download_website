import requests
from bs4 import BeautifulSoup
import os


def download(url):
    # 发送 GET 请求获取网页内容
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    # 解析 HTML 内容
    soup = BeautifulSoup(response.content, 'html.parser')
    # 获取程序所在的目录路径
    directory = os.path.dirname(os.path.abspath(__file__))
    # 找到 lu 标签 class 值为 nav 下的所有 a 标签
    lu_nav = soup.find('ul', {'id': 'mysidebar'})
    print(lu_nav)
    a_tags = lu_nav.find_all('a')
    
    for link in   a_tags:
        href = link.get('href')
        if href == '#':  # 如果链接为 #
            continue
        # 如果链接以 / 开头，则需要加上主机地址
        if href.startswith('/'):
            href = url + href
        # 获取链接对应的内容并保存为本地文件
        content = requests.get(href, headers=headers).content
        filename = href.replace(url, '').strip('/')
        filename = filename.replace('/', '-')
        filename = os.path.join(directory, filename)
        with open(filename, 'wb') as f:
            f.write(content)
        # 查找所有符合条件的 ul 标签
        uls = link.find_all('ul')
        for ul in uls:
            # 查找 ul 中的所有符合条件的 a 标签链接
            a_links = ul.find_all('a')
            for a_link in a_links:
                href = a_link.get('href')
                if href == '#':  # 如果链接为 #
                    continue
                # 如果链接以 / 开头，则需要加上主机地址
                if href.startswith('/'):
                    href = url + href
                # 获取链接对应的内容并保存为本地文件
                content = requests.get(href, headers=headers).content
                filename = href.replace(url, '').strip('/')
                filename = filename.replace('/', '-')
                filename = os.path.join(directory, filename)
                with open(filename, 'wb') as f:
                    f.write(content)


if __name__ == '__main__':
    url = 'https://redbu1l.github.io'
    download(url)
