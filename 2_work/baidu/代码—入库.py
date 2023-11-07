import re
import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")
cursor=db.cursor()

with open("date.txt","r") as f:
    for i in f:
        use_sql="USE baidutoday;"
        creat_sql="create table date%s (num INT,year INT,type CHAR(5),title CHAR(100),subject CHAR(200));"%(i.strip())
        # print(creat_sql)
        cursor.execute(use_sql)
        cursor.execute(creat_sql)

        db.commit()
db.close()
print("fine")




#以上已创建好数据库，目的创建表和列







#最终代码

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

cursor=db.cursor()
use_sql="use baidutoday;"
cursor.execute(use_sql)

count=0
fault=0

import re
def death(string):
    match=re.search(r"逝世",string)
    if match:
        return 1
    else:
        return 0
def birth(string):
    match=re.search(r"出生",string)
    if match:
        return 1
    else:
        return 0



try:
    driver=webdriver.Firefox()
    driver.get("https://baike.baidu.com/calendar/")
    time.sleep(1)#多睡一会儿加载动态信息
    butto=driver.find_element(By.CSS_SELECTOR,".prev ")
    # butto_=driver.find_element(By.CSS_SELECTOR,".next ")
    for null in range(2):
        butto.click()
        time.sleep(1)
        butto=driver.find_element(By.CSS_SELECTOR,".prev ")
    time.sleep(1)
    with open("日期库.txt","r") as f:#日期是2023-1-3这样的日期，用于找到网页的按键
        with open("date.txt","r") as fl:#date文件是1_3这样的日期，用于数据库行的定位
            lines=fl.readlines()
            for line in f:
                count+=1
                print(4)
                
                date=lines[count-1]
                print(5)
                
                selector='li[data-date="%s"]'%(line.strip())
                time.sleep(1)
                button_date=driver.find_element(By.CSS_SELECTOR,selector)
                # if count==1:
                #     pass
                # else:
                button_date.click()
                print(6)
                time.sleep(2)
                html = driver.page_source#获取网页信息
                time.sleep(2)
                
                
                soup=BeautifulSoup(html,"html.parser")#利用bs4开始分析数据
                if soup:
                    print("did")
                    # print(soup)
                # time.sleep(1)
            
                
                subject_event=soup.find_all(name="dl",attrs={"class":"events"})
                subject_date=soup.find(name="span",attrs={"class":"date"})
                subject_event_=soup.find_all(name="div",attrs={"class":"event_cnt"})
                print(subject_date.text)
                time.sleep(1)
                for i in subject_event:
                    subject_year=i.find_all(name="div",attrs={"class":"year"})
                    subject_event=i.find_all(name="div",attrs={"class":"event_tit"})
                n=0
                # time.sleep(1)
                for ii in subject_year:
                    n+=1
                    insert_sql="insert into date%s (num,year) values (%d,'%s');"%(date,n,ii.text)
                    
                    print(ii.text)
                    cursor.execute(insert_sql)
                n=0    
                # time.sleep(1)
                for iii in subject_event:
                    n+=1
                    text=iii.text
                    if birth(text)==1:
                        type="birth"
                    elif death(text)==1:
                        type="death"
                    else:
                        type="event"
                    update_sql="update date%s set type='%s',title='%s' where num=%d;"%(date,type,text,n)
                    print(text)#iii.text
                    cursor.execute(update_sql)
                    
                n=0
                if date=='1_6':
                    fault+=1
                
                for iiii in subject_event_:
                    thing=iiii.get_text()
                    # match=re.search(r"\'",thing)
                    # if match:
                    #     thing=re.sub(r"\'","\\\'")
                    n+=1
                    
                    
                    updatee_sql="update date%s set subject=%%s where num=%%s"%date
                    cursor.execute(updatee_sql,(thing,n))
                    print(date)
                print("fine")

                db.commit()
    db.close()
    driver.quit()


except:
    print("wrong")
    driver.quit()
