
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from time import gmtime, strftime
from tkinter import messagebox
driver = webdriver.PhantomJS(executable_path=r'C:\Users\plusline\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJs
tag = ".course_y2"

address="http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no=E2"
order=-2
#-2 人工智慧
#-3 訊號與系統

#fist time

driver.get(address)  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(pageSource, "lxml")
courses=soup.select('{}'.format(tag))
#course=courses[order]
#print(course)

def check(order, name, courses):
    course=courses[order]
    if "full" not in course.text:
        print("take the course:"+name)
        messagebox.showinfo("HURRY", "take the course:"+name)
    else :
        print(name+"fail")

while True:
    print("reflash")
    driver.get(address)  # 輸入範例網址，交給瀏覽器 
    pageSource = driver.page_source  # 取得網頁原始碼
    soup = BeautifulSoup(pageSource, "lxml")


    courses=soup.select('{}'.format(tag))

    check(-2 ,"人工智慧",courses)
    check(-3 ,"訊號與系統",courses)
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    time.sleep( 60 )
    print()

driver.close()  # 關閉瀏覽器
