#导入数据库

import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

n=0
cursor=db.cursor()
with open("title.txt","r") as f:
    for i in f:
        n+=1
        table="list_%d"%(n)
        use_database_sql="USE fzu_edu;"
        create_table_sql="CREATE table %s (title VARCHAR(100));"%(table)
        add_imformation_sql="INSERT INTO %s (title) VALUES ('%s');"%(table,i.strip())#字符串用单引号提示
        cursor.execute(use_database_sql)
        cursor.execute(create_table_sql)
        cursor.execute(add_imformation_sql)#运行语句一句句来
db.commit()
db.close()
#######################################################################




#导标题+序号
#导入数据库

import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

n=0
cursor=db.cursor()
with open("title.txt","r") as f:
    for i in f:
        n+=1
        num=n
        use_database_sql="USE fzu_edu"
        add_imformation_sql="INSERT INTO work (num,title) VALUES (%d,'%s');"%(n,i.strip())#字符串用单引号提示
        cursor.execute(use_database_sql)
        # cursor.execute(add_column_sql)
        cursor.execute(add_imformation_sql)#运行语句一句句来
db.commit()
db.close()



#副链接
#实际运行代码
import requests
import pymysql
from bs4 import BeautifulSoup

try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")


n=0
cursor=db.cursor()

with open("link_store.txt","r") as f:
    for i in f:
        n+=1
        link="https://jwch.fzu.edu.cn"+i.strip()
        response=requests.get(link)
        response.encoding="utf-8"
        all=response.text
        soup=BeautifulSoup(all,"html.parser")#数据树


        sur=soup.find_all(name="div",attrs={"class":"xl_main"})#附件链接附件名下载次数
        for link in sur:
            llink=link.find_all(name="ul")
            if llink:
                for ans in llink:
                    sub_link=ans.find_all(name="a")
                for final in sub_link:
                    use_database_sql="USE fzu_edu"
                    update_sql="UPDATE work set sub_title = '%s' WHERE num = %d;"%(final["href"].strip(),n)
                    cursor.execute(use_database_sql)
                    cursor.execute(update_sql)
    db.commit()
    db.close()                

print("fine")



#导链接
import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

n=0
cursor=db.cursor()
with open("link_store.txt","r") as f:
    for i in f:
        n+=1
        use_database_sql="USE fzu_edu"
        update_imformation_sql="UPDATE work set link = '%s' WHERE num = %d;"%(i.strip(),n)#字符串用单引号提示
        cursor.execute(use_database_sql)
        # cursor.execute(select_line_sql)
        cursor.execute(update_imformation_sql)#运行语句一句句来
db.commit()
db.close()



#导通知人

import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

n=0
cursor=db.cursor()
with open("advocator.txt","r") as f:
    for i in f:
        n+=1
        use_database_sql="USE fzu_edu"
        update_imformation_sql="UPDATE work set advocator = '%s' WHERE num = %d;"%(i.strip(),n)#字符串用单引号提示
        cursor.execute(use_database_sql)
        # cursor.execute(select_line_sql)
        cursor.execute(update_imformation_sql)#运行语句一句句来
db.commit()
db.close()



#导日期
import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")

n=0
cursor=db.cursor()
with open("date.txt","r") as f:
    for i in f:
        n+=1
        use_database_sql="USE fzu_edu"
        update_imformation_sql="UPDATE work set date = '%s' WHERE num = %d;"%(i.strip(),n)#字符串用单引号提示
        cursor.execute(use_database_sql)
        # cursor.execute(select_line_sql)
        cursor.execute(update_imformation_sql)#运行语句一句句来
db.commit()
db.close()



#导附件（副）标题
import requests
import pymysql
from bs4 import BeautifulSoup

try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")


n=0
cursor=db.cursor()

with open("link_store.txt","r") as f:
    for i in f:
        n+=1
        final_text=""
        link="https://jwch.fzu.edu.cn"+i.strip()
        response=requests.get(link)
        response.encoding="utf-8"
        all=response.text
        soup=BeautifulSoup(all,"html.parser")#数据树


        sur=soup.find_all(name="div",attrs={"class":"xl_main"})#附件链接附件名下载次数
        for link in sur:
            llink=link.find_all(name="ul")
            if llink:
                for ans in llink:
                    sub_link=ans.find_all(name="a")
                for final in sub_link:
                    # print(final.get_text())
                    text=final.get_text()
                    final_text=final_text+"+"+text
                    # print(text,"one")
                    use_database_sql="USE fzu_edu"
                    update_imformation_sql="UPDATE work set sub_title = '%s' WHERE num = %d;"%(final_text.strip(),n)#字符串用单引号提示
                    cursor.execute(use_database_sql)
                    # cursor.execute(select_line_sql)
                    cursor.execute(update_imformation_sql)#运行语句一句句来

db.commit()
db.close()
          
print("fine")


#导附件链接
import requests
import pymysql
from bs4 import BeautifulSoup

try:
    db=pymysql.connect(host="localhost",user="root",passwd="18695776905Qlg",port=3306)
    print("fine")
except:
    print("wrong")


n=0
cursor=db.cursor()

with open("link_store.txt","r") as f:
    for i in f:
        n+=1
        final_link=""
        link="https://jwch.fzu.edu.cn"+i.strip()
        response=requests.get(link)
        response.encoding="utf-8"
        all=response.text
        soup=BeautifulSoup(all,"html.parser")#数据树


        sur=soup.find_all(name="div",attrs={"class":"xl_main"})#附件链接附件名下载次数
        for link in sur:
            llink=link.find_all(name="ul")
            if llink:
                for ans in llink:
                    sub_link=ans.find_all(name="a")
                for final in sub_link:
                    # print(final.get_text())
                    link=final["href"].strip()
                    final_link=final_link+"+"+link
                    # print(text,"one")
                    use_database_sql="USE fzu_edu"
                    update_imformation_sql=update_sql="UPDATE work set sub_link = '%s' WHERE num = %d;"%(final_link.strip(),n)
                    cursor.execute(use_database_sql)
                    # cursor.execute(select_line_sql)
                    cursor.execute(update_imformation_sql)#运行语句一句句来

db.commit()
db.close()
          
print("fine")

