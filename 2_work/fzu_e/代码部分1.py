import requests
import re
from bs4 import BeautifulSoup


#教务处第一页——通知链接+标题+通知人+日期#我想先获取到各个信息，再一一存入相应的文件，最后通过存储信息的文件导入数据库
url="https://jwch.fzu.edu.cn/jxtz.htm"
response=requests.get(url)
response.encoding="utf-8"#使文本正确显示
all=response.text
soup=BeautifulSoup(all,"html.parser")#解析器+树

#计数3676
total=0

subject_ul=soup.find_all(name="ul",attrs={"class":"list-gl"})
for i in subject_ul:
    subject_li=i.find_all(name="li")
for ii in subject_li:
    # print(ii.get_text()) #显示一下
    text_li=ii.get_text()
    match_date=re.search(r".[0,9].*",text_li.strip())
    print("日期:",match_date.group())
    match_advocator=re.search(r"【.*",text_li.strip())
    print("通知人:",match_advocator.group())
    subject_ul_a=ii.find_all(name="a")
    for iii in subject_ul_a:
        text_ul_a=iii.get_text()
        # match_title=re.search(r"\s.*",text_ul_a.strip())
        print("标题:",text_ul_a)
        print("\n")
total+=20


#第二页及以后
for i in range(183,0,-1):
        
    url="https://jwch.fzu.edu.cn/jxtz/%d.htm"%(i)
    response=requests.get(url)
    response.encoding="utf-8"#使文本正确显示
    all=response.text
    soup=BeautifulSoup(all,"html.parser")#解析器+树
    
    subject_ul=soup.find_all(name="ul",attrs={"class":"list-gl"})
    for i in subject_ul:
        subject_li=i.find_all(name="li")
        total+=len(subject_li)


    
    for ii in subject_li:
        # print(ii.get_text()) #显示一下
        text_li=ii.get_text()
        match_date=re.search(r".[0,9].*",text_li.strip())
        print("日期:",match_date.group())
        match_advocator=re.search(r"【.*",text_li.strip())
        print("通知人:",match_advocator.group())
        subject_ul_a=ii.find_all(name="a")
        for iii in subject_ul_a:
            text_ul_a=iii.get_text()
            # match_title=re.search(r"\s.*",text_ul_a.strip())
            print("标题:",text_ul_a)
            print("\n")

    if(total>=100):
        print("fine")
        break
#将各个通知链接存入link_store，接下来通过这些链接获取下一步的信息