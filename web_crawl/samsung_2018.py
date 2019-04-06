from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk 한글 관려 오류가 난경우 다운로드
# import nltk
#nltk.download()

okt = Okt()
ctx='C:/Users/ezen/PycharmProjects/ezen_0406/data/'
filename = ctx+'kr-Report_2018.txt'

with open(filename,'r', encoding='UTF-8') as f:
    texts = f.read()

texts = texts.replace('\n','')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('', texts)

tokens = word_tokenize(texts)



none_token=[]
for token in tokens:
    token_pos = okt.pos(token)
    temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == "Noun"]
    if len(''.join(temp)) >1:
        none_token.append("".join(temp))
texts = " ".join(none_token)


#불용어 제거
with open(ctx+'stopwords.txt','r', encoding='UTF-8') as f:
    stopwors = f.read()

stopwors = stopwors.split(' ')


texts = [text for text in tokens if text not in stopwors]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)

#print(freqtxt[:30])

okt.pos('가치창출')
okt.pos('갤럭시') # 오타는 갤럭시로 처리
wcloud = WordCloud(ctx+'D2Coding.ttf',relative_scaling =0.2,
                   background_color ='white').generate(" ".join(texts))
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()









