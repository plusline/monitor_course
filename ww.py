
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.PhantomJS(executable_path=r'C:\Users\user\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJs
tag = ".course_y2"

address="http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no=E2"
order=-3

#fist time

driver.get(address)  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(pageSource, "lxml")
courses=soup.select('{}'.format(tag))
course=courses[order]
print(course)


while True:
    print("reflash")
    driver.get(address)  # 輸入範例網址，交給瀏覽器 
    pageSource = driver.page_source  # 取得網頁原始碼
    soup = BeautifulSoup(pageSource, "lxml")


    courses=soup.select('{}'.format(tag))

    course=courses[order]

    time.sleep( 1 )
    if "額滿" not in course.text:
        print("take the course")
driver.close()  # 關閉瀏覽器
