# 함수 호출
import time
import random

#숫자를 가리는 함수
def clear():
    for i in range(0,100):
        print("                                                                        ")

#초기값 및 변수 초기화 
count = 3
score = 0

st1_num = ""
st2_num = ""
st3_num = ""
st4_num = ""

st1_name =""
st2_name =""
st3_name =""
st4_name =""

#시작 화면
print("숫자 기억하기 게임")
print(" ")
print("[게임설명]")
print("- 4초 마다 숫자가 사라집니다.")
print("  숫자를 잘 기억하고 입력해주세요! ")
print("")
print("- 정답을 맞추면 점수 10점을 얻습니다.")
print("  또한 점수에 따라 난이도가 높아집니다.")
print("")
print("- 숫자와 숫자 사이는 space바로 띄워서 입력해주세요!")
print("")
print("- 최대 4명의 친구와 즐길 수 있습니다! ")
print("")
time.sleep(10)
clear()


#메인 코드
people = int(input("게임 인원을 입력해주세요."))
score_num = ""
for j in range(0,people):
    name = str(input("이름:"))
    i=0
    score=0
    count=3
    while (i<=5):
        i=i+1
        print("3개의 숫자부터 시작합니다.")
        num=""
        for  x in range(count):
            rand_num = random.randint(1,50)
            num += str(rand_num)
            num +=" "

        print(num)
        time.sleep(4)
        clear()
    
        user_input = input("기억한 숫자를 입력하세요")

        if(user_input == num.strip()):
            print("정답입니다.")
            print("")
            score += 10
        else:
            print("틀렸습니다.")
            print("정답은"+ num + "입니다.")
            print("")
    
        if score > 30:
            count = score // 30 + 3


        if (i==6):
            score_sum = str(score)
            print("%s님의 점수: %s" %(name,score_sum))
            
    if(j==0):
        st1_num = score_sum
        st1_name = name
    elif(j==1):
        st2_num = score_sum
        st2_name = name
    elif(j==2):
        st3_num = score_sum
        st3_name = name
    elif(j==3):
        st4_num = score_sum
        st4_name = name

print("")
print("      <게임결과>")
print("")
if people>=1:
    print(st1_name+"님의 점수는 "+st1_num+"입니다.")
if people>=2:
    print(st2_name+"님의 점수는 "+st2_num+"입니다.")
if people>=3:
    print(st3_name+"님의 점수는 "+st3_num+"입니다.")
if people>=4:
    print(st4_name+"님의 점수는 "+st4_num+"입니다.")
