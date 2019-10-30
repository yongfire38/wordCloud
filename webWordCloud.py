#HTML 파싱을 위한 라이브러리
from bs4 import BeautifulSoup
#웹에서 데이터를 가져오기 위한 라이브러리
import urllib.request
#url인코딩을 위한 라이브러리
from urllib.parse import quote
#형태소 분석해 주는 라이브러리
from konlpy.tag import Okt
from konlpy.corpus import kolaw

#검색할 문자열과 검색할 기사 개수 및 텍스트를 저장할 파일명을 입력받기
keyword = input("검색어:")
page_num = int(input("기사 개수(곱하기 3):"))
output_filename = input("저장할 파일명:")

#텍스트를 저장할 파일 객체 만들기
output_file = open(output_filename, 'w', encoding='utf-8')

#기사 개수만큼 순회
for i in range(page_num):
    #주소 만들기
    current_page_num = 1 + i*3
    target_url = "http://news.donga.com/search?check_news=1&more=1&sorting=3&range=1&search_date=&query=" + quote(keyword) + "&q=" +str(current_page_num)
    #데이터 가져오기
    source_code = urllib.request.urlopen(target_url)
    #print(source_code)
    #위 코드에서 태그 이름은 p이고 클래스 이름은 tit인 모든 태그를 가져오기
    soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
    for title in soup.find_all('p', 'tit'):
        #print(title)
        #title로 뽑아낸 데이터에서 첫번째 a 태그의 href속성이 기사 링크 url임
        title_link = title.select('a')
        article_url = title_link[0]['href']
        #print(article_url)

        articleTxt = urllib.request.urlopen(article_url)  
        articleSoup =  BeautifulSoup(articleTxt, 'lxml', from_encoding='utf-8') 
        article = articleSoup.select('div.article_txt')
        #print(article)
        #기사 내용을 추출하여 파일에 저장
        for item in article:
            stritem = str(item.find_all(text=True))
            output_file.write(stritem)

output_file.close()

#파일 내용 읽어 오기
f = open(output_filename, 'r', encoding='utf-8')
data = f.read()
#print(data)
#형태소 분석기 생성

nlp = Okt()
nouns = nlp.nouns(data)
print(nouns)
