import requests

from bs4 import BeautifulSoup


with open("javascript.txt","w") as f:
        #附件信息
    num=0#序号标记——哪个链接存在附件
    with open("link_storex.txt","r") as ff:
        for link in ff:
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
                    # subject_a=i.find_all(name="a")#傅建明及其链接
                    subject_span=i.find_all(name="script")#下载次数的jsp函数
                # for ii in subject_a:    
                    # print("标题:",ii.get_text())
                    # print("链接:",ii["href"])#获取的链接需要简单处理一下（前面加上http什么的）再写入存链接的文件里
                for iii in subject_span:
                    text="%d"%(num)+iii.get_text()
                    f.write(text.strip()+"\n")
                
            else:
                print("none\n")
    #成功获取

