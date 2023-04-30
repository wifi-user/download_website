import os
import requests
from bs4 import BeautifulSoup

# 获取程序所在的目录路径
directory = os.path.dirname(os.path.abspath(__file__))
# 设置下载的 CSS 文件存储路径
css_dir = os.path.join(directory, "css")

# 如果存储 CSS 文件的目录不存在，则创建它
if not os.path.exists(css_dir):
    os.makedirs(css_dir)

# 遍历当前目录下的所有 .html 文件
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            # 使用 BeautifulSoup 解析 HTML 内容
            soup = BeautifulSoup(f.read(), "html.parser")
            # 查找所有的 link 标签
            links = soup.find_all("link")
            for link in links:
                # 判断 link 标签的 rel 属性是否为 "stylesheet"
                if link.get("rel") == ["stylesheet"]:
                    # 获取 link 标签的 href 属性值
                    href = link.get("href")
                    # 如果 href 是相对路径，则拼接成绝对路径
                    if not href.startswith("http"):
                        href = os.path.join('https://redbu1l.github.io/', href)
                    # 构造 CSS 文件名，以 URL 中最后一个 / 后面的内容作为文件名
                    css_filename = href.split("/")[-1]
                    # 判断 CSS 文件是否已经存在于本地，如果不存在，则下载
                    css_path = os.path.join(css_dir, css_filename)
                    if not os.path.exists(css_path):
                        print(f"Downloading {href}...")
                        r = requests.get(href)
                        with open(css_path, "wb") as f:
                            f.write(r.content)
