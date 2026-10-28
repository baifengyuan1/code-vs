import requests
import re

f=open("movie.csv",mode='w',encoding='utf-8')

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"}

for i in range(1,11):
    temp=(i-1)*25
    url="https://movie.douban.com/top250?start={temp}"
    resp=requests.get(url,headers=headers)
    content=resp.text
    obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p>.*?导演: (?P<director>.*?)&nbsp;' \
    '.*?主演: (?P<actor>.*?)<br>(?P<year>.*?)&nbsp;',re.S)
    result=obj.finditer(content)
    for item in result:
        name=item.group("name")
        director=item.group("director")
        actor=item.group("actor")
        year=item.group("year").strip()
        f.write(f"{name}{director}{actor}{year}\n")


