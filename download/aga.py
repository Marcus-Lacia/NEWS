from lxml.html.clean import Cleaner
import requests

url ='https://alice.colopl.jp/news/importants'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

html = requests.get(url, headers=headers).content
#清除不必要的标签
cleaner = Cleaner(style = True,scripts=True,comments=True,javascript=True,page_structure=False,safe_attrs_only=False)

content = cleaner.clean_html(html.decode('utf-8')).encode('utf-8')
#这里打印出来的结果会将上面过滤的标签去掉，但是未过滤的标签任然存在。

fileout=open('agaim.txt','wb')
fileout.write(content)