#태그 클라우드
import pytagcloud
#개수를 세 주기 위해
from collections import Counter

#단어의 list를 생성
nouns = list()
nouns.extend(['불고기' for p in range(8)])
nouns.extend(['비빔밥' for t in range(7)])
nouns.extend(['김치찌개' for t in range(7)])
nouns.extend(['돈까스' for t in range(6)])
nouns.extend(['순두부백반' for t in range(6)])
nouns.extend(['짬뽕' for t in range(6)])
nouns.extend(['짜장면' for t in range(6)])
nouns.extend(['삼겹살' for t in range(5)])
nouns.extend(['초밥' for t in range(5)])
nouns.extend(['우동' for t in range(5)])

#print(nouns)

#collections 모듈의 Counter를 이용하면 각 단어의 개수를 가지는 객체 생성 가능
count = Counter(nouns)
#print(count)

#추출할 개수를 설정(most_common 메서드는 빈도수가 높은 순으로 반환)
taglist = count.most_common(20)
#print(taglist)

#글자의 최대 크기를 설정
tag1 = pytagcloud.make_tags(taglist, maxsize=50)

#워드 클라우드 생성
pytagcloud.create_tag_image(tag1, 'wordcloud.png', fontname='Korean', size=(900,600))