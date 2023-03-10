from datetime import datetime
import random

# 영화 정보 입력 받는 곳
main_title = input("영화의 제목: ")
director = input("영화의 감독 이름: ")
genre = input("영화의 장르: ")
main_actor = input("영화의 주인공 이름: ")
main_audiences = input("["+main_title+"] 누적 관객수: ")
sub_title = input("비교할 비슷한 장르의 영화제목: ")
sub_audiences = input("["+sub_title+"] 누적 관객수: ")

# 다양한 문장을 랜덤 선택  
wordingMain = ["넘어서며 폭풍 흥행을 달리고 있습니다.","넘어서며 흥행성적을 달리고 있습니다.","열심히 흥행을 달리고있습니다."]
wordingSub = ["과연 넘어설 수 있을지 이목이 집중됩니다.","더 큰 흥행성적을 거둘 수 있을지 이목이 집중됩니다","더 많은 관심을 받을 수 있을지 이목이 집중됩니다."]

# 기사 작성하는 곳
news= "\n["+main_title+"의 현재 흥행 성적("+str(datetime.now())+")]\n"
news= news+"\n 큰 기대속에 개봉된 ["+main_title+"]은(는) "+genre+" 장르의 영화로 큰 주목을 받았습니다.\n"
news= news+"이번 영화 ["+main_title+"]은(는) "+director+" 감독, "+main_actor+" 주연의 작품입니다.\n"
news= news+"과연 ["+main_title+"]이(가) 과거의 영화 ["+sub_title+"]의 누적 관객수를 넘을수 있을지 관심이 쏠리는 상황입니다.\n"

if main_audiences > sub_audiences:
    news=news+"현재 엄청난 흥행 성적을 거두고있는 ["+main_title+"]이(가) 놀랍게도 "+sub_title+"의 누적 관객수를 돌파하였습니다.\n"
elif main_audiences < sub_audiences:
    news=news+"허나 아직은 아쉽게도 "+main_title+"은(는) "+sub_title+"의 누적 관객수를 돌파하지 못하였습니다.\n"
else:
    news=news+"현재 두 영화의 관객수 서로 "+main_audiences+"로 같은 상태입니다.\n"

if int(main_audiences) < int(sub_audiences):
    if int(sub_audiences) > 10000000:
        news=news+"천만 관객을 돌파한 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingSub)
    elif int(sub_audiences) > 5000000:
        news=news+"오백만 관객을 돌파했던 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingSub)
    elif int(sub_audiences) > 1000000:
        news=news+"백만 관객을 돌파했던 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingSub)
    else:
        news=news+"두 영화는 각각 "+main_audiences+", "+sub_audiences+" 으로 백만 관객 이상의 성적을 이루지 못하였습니다"
        
if int(main_audiences) > int(sub_audiences):
    if int(main_audiences) > 10000000:
        news=news+"천만 관객을 돌파한 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingMain)
    elif int(main_audiences) > 5000000:
        news=news+"오백만 관객을 돌파했던 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingMain)
    elif int(main_audiences) > 1000000:
        news=news+"백만 관객을 돌파했던 영화 ["+sub_title+"]을(를) 현재 관객 수 "+main_audiences+"명의 ["+main_title+"]이(가) "+random.choice(wordingMain)
    else:
        news=news+"두 영화는 각각 "+main_audiences+", "+sub_audiences+" 으로 백만 관객 이상의 성적을 이루지 못하였습니다"

print(news)

# 음성으로 들려주는 곳
from gtts import gTTS
import playsound

tts=gTTS(text=news,lang='ko') # 문자열 news를 위한 한국어 음성 합성
tts.save("news(Movie Boxoffice Performance)_Kimdohun_201807558.mp3")
playsound.playsound("news(Movie Boxoffice Performance)_Kimdohun_201807558.mp3",True)