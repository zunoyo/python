# pip install selenium
#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# -- 크롬에서 작업하기 위한 작업들 ↑



#네이버 기사 크롤링
'''

driver.get('https://www.naver.com')

import time 
time.sleep(2) #5초동안 네이버 켜놓기 
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click() #네이버의 뉴스버튼 full xpath 가져온 값
time.sleep(3)
newstitle = driver.find_element(By.XPATH,'/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div').text
print(newstitle)
'''


'''
#아파트 시세 크롤링 
import time 
driver.get('https://m.land.naver.com/search')
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input').send_keys('압구정 현대 13차')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i').click()
time.sleep(1)
saleprice = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd').text
jeonse = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd').text
print(saleprice)
print(jeonse)
'''


driver.get('https://m.stock.naver.com/')


a1= driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[9]/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/div/span[1]').text
a2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[9]/div[3]/div[1]/table/tbody/tr[2]/td[1]/div/div/span[1]').text
a3 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[9]/div[3]/div[1]/table/tbody/tr[3]/td[1]/div/div/span[1]').text

print(a1,a2,a3)




lst = []
lst2 = []
for i in range(5):
    subject = driver.find_element(By.XPATH,f'/html/body/div/div[2]/div/div[9]/div[3]/div[1]/table/tbody/tr[{i+1}]/td[1]/div/div/span[1]').text
    lst.append(subject)
for i in range(5):
        price = driver.find_element(By.XPATH,f'/html/body/div/div[2]/div/div[9]/div[3]/div[1]/table/tbody/tr[{i+1}]/td[2]/span').text
        lst2.append(price)

print(lst)   
print(lst2)

