import requests
import re
from bs4 import BeautifulSoup
import json

#处理网页JavaScript函数获取相应信息这里是下载次数
def jsp(function):#从ajax文件可以得知存储下载次数json信息的网页url格式，这里向其发送异步请求得到json格式的信息
    match_id=re.search(r"[0-9]+",function)#观察发现只有第一个参数不一样
    url="https://jwch.fzu.edu.cn/system/resource/code/news/click/batchclicktimes.jsp?wbnewsid=%d&owner=1744984858&type=wbnewsfile&randomid=attach"%(int(match_id.group(0)))
    response_js=requests.get(url)
    thing=response_js.json()#获得字典的列表
    for i in thing:
        ans=i['clicktime']
        print("下载量:",ans)#


#附件信息
num=0#序号标记——哪个链接存在附件
with open("link_storex.txt","r") as f:
    for link in f:
        num+=1
        print(num)
        url="https://jwch.fzu.edu.cn"+link.strip()
        response=requests.get(url)
        response.encoding="utf-8"#使文本正确显示
        all=response.text
        soup=BeautifulSoup(all,"html.parser")#解析器+树

        subject_ul=soup.find_all(name="ul",attrs={"style":"list-style-type:none;"})#
        if subject_ul:
            for i in subject_ul:
                subject_a=i.find_all(name="a")#傅建明及其链接
                subject_span=i.find_all(name="script")#下载次数的jsp函数
            for ii in subject_a:    
                print("标题:",ii.get_text())
                print("链接:",ii["href"])#获取的链接需要简单处理一下（前面加上http什么的）再写入存链接的文件里
            for iii in subject_span:
                sub=iii.get_text().strip()
                print("jsp:",sub)
                jsp(sub)#之后在导入数据库的时候同时存傅建明，附件链接和下载次数
            print("\n")
        else:
            print("none\n")
#成功获取