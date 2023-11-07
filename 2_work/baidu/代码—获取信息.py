from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


#数据量太大稍后直接入库,这里是先获取数据,显示一下
try:
    driver=webdriver.Firefox()
    driver.get("https://baike.baidu.com/calendar/")
    time.sleep(2)#多睡一会儿加载动态信息
    butto=driver.find_element(By.CSS_SELECTOR,".prev ")
    butto_=driver.find_element(By.CSS_SELECTOR,".next ")
    
    butto_.click()
    time.sleep(2)
    html = driver.page_source#获取网页信息
    
    
    soup=BeautifulSoup(html,"html.parser")#利用bs4开始分析数据
   
    
    subject_event=soup.find_all(name="dl",attrs={"class":"events"})
    subject_date=soup.find(name="span",attrs={"class":"date"})
    subject_event_=soup.find_all(name="div",attrs={"class":"event_cnt"})
    print(subject_date.text)#日期
    for i in subject_event:
        
        subject_year=i.find_all(name="div",attrs={"class":"year"})
        subject_event=i.find_all(name="div",attrs={"class":"event_tit"})
        for ii in subject_year:
            print(ii.text)#年份
        for iii in subject_event:
            print(iii.text)#标题
            
        for iiii in subject_event_:
            
            print(iiii.get_text())#简要内容


    driver.quit()


except:
    driver.quit()