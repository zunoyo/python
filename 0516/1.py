#웹 크롤링

from bs4 import BeautifulSoup
import requests #http 요청 처리 library
headers = {
    "User-Agent":"zuno"

}

webpage = requests.get("https://sports.news.naver.com/news?oid=144&aid=0000887187",headers=headers)
print(webpage)

soup = BeautifulSoup(webpage.content,'html.parser') #html로 파싱된 결과 보기
print(soup)
news = soup.select_one("#newsEndContents").get_text().strip() #id 값을 넣어야함 
print(news)