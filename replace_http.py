import os
import re
# 获取程序所在的目录路径
directory = os.path.dirname(os.path.abspath(__file__))

# 遍历目录下的所有.html文件
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        print(filepath)
        # 打开文件，读取文件内容并替换"hello"为""
        with open(filepath, "r+") as f:
            content = f.read()
            # 匹配以http开头、以.com结尾的URL链接
            pattern = r'src="http\S+com/'
            # 用空字符串替换匹配到的URL链接
            new_content = re.sub(pattern, 'src="',content)
            # 将光标移到文件开头，覆盖写入新内容
            f.seek(0)
            f.write(new_content)
            # 如果新内容比原内容短，清除文件尾部多余的内容
            f.truncate()
