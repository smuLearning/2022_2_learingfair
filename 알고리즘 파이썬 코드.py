import random 
import numpy as np

#게임 시작화면 및 초기값들
#결과 출력
def result(i):
    if(i ==1):
        return 5
    elif(i==2):
        return 4
    elif(i==3):
        return 3
    elif(i==4):
        return 2
    elif(i==5):
        return 1


#------------------------------------------------------------------------------------------------------------------------
print("게임을 시작합니다.")
print("카드가 섞입니다.")

Deck_Card = np.random.choice(range(1,6),5,replace = False) #Deck_Card = 무작위로 섞이 카드, 앞에 놓여있는 카드들
print(Deck_Card)#최종에서 지우기
RandNum = random.randint(1,5) #최종에는 아래로 내리기 #RandNum = 옵션 세게를 고를 사람 정하는 랜덤문
print(RandNum)#최종에서 지우기
while True:
    M_Card = int(input("원하시는 카드의 번호를 선택하세요: "))#배열의 번재 정하기 M_Card = 원하는 카드를 정하는것

    if(M_Card >5 or M_Card<1):
        print("범위내의 카드를 다시 골라주세요.")
        continue

    else:
        print("당신은 {}번 카드를 선택하셨습니다!".format(M_Card))
        break
        
M_C_Number = Deck_Card[M_Card - 1]#M_C_Number = 배열상의 자신이 정한 카드 고르기
print(M_C_Number)#최종에서 지우기
print("기억하세요! 당신의 숫자는 {} 입니다".format(M_C_Number))#최종에서 지우기


#------------------------------------------------------------------------------------------------------------------------

if RandNum == M_C_Number:
    print("============================================")
    print("1. 다른 플레이어와 카드를 교환하시겠습니까? ")
    print("2. 모든 플레이어의 카드를 바꾸겠습니까?")
    print("3. 판을 엎고 게임을 끝내시겠습니까? ")
    print("4. 게임을 끝내시겠습니까?")
    print("============================================")
    
    while True:
        choice1 = int(input("원하시는 옵션을 선택해주세요."))#옵션 3개중 한개 고르기
        if(choice1 >4 or choice1<1):
            continue
        
        else:
            print("{}번을 선택하셨습니다: ".format(choice1))
            break
    
    
    if choice1 == 1:#만약 선택이 1번이라면
        print("원하는 사람과 카드를 교환합니다.")
        while True:
            choice2 = int(input("방향을 정해주세요. : (오른쪽 : 1, 왼쪽 : 2를 눌러주세요.)"))#choice2는 방향 정하기
            #문자열로 받을지 숫자로 받을지는 추후에 정한다. 
            if choice2 > 2 or choice2<1:
                print("범위내의 숫자를 다시 입력해주세요.")
                continue
            else:
                break
                
        while True:
            num = int(input("몇번째 플레이어와 바꾸시겠습니까?(1번째~2번째) ")) #num = 몇번째 인원인지
            if num > 2 or num<1:
                print("범위내의 숫자를 다시 입력해주세요")
                continue
            else:
                break         
        
        
            
        
        if choice2 == 1:
            print("오른쪽을 선택하셨습니다.")
            print("오른쪽 {}번째 인원과 카드를 교환하겠습니다.",format(num))
            print(M_Card)#최종삭제
            print(len(Deck_Card))#최종삭제
            print(M_Card+num)#최종삭제
            if(M_Card + num > len(Deck_Card)):
                Deck_Card[M_Card - 1], Deck_Card[M_Card -1 + num-(len(Deck_Card))] = Deck_Card[M_Card -1 + num-(len(Deck_Card))], Deck_Card[M_Card - 1] 
            else:
                Deck_Card[M_Card - 1], Deck_Card[M_Card -1 + num] = Deck_Card[M_Card -1 + num], Deck_Card[M_Card - 1] 
                
            print(Deck_Card)#최종삭제
            
        else:
            print("왼쪽을 선택하셨습니다.")
            print("왼쪽 {}번째 인원과 카드를 교환하겠습니다.")
            Deck_Card[M_Card - 1], Deck_Card[M_Card -1 - num] = Deck_Card[M_Card -1 - num], Deck_Card[M_Card - 1] 
            #index 6 is out of bounds for axis 0 with size 5 문제
            print(Deck_Card)
            
        print("당신의 카드 숫자는 {} 입니다".format(Deck_Card[M_Card-1]))
        game_result = result(Deck_Card[M_Card-1])
        print("==================결과======================")
        print("당신은 {}등입니다.".format(game_result))

        
 #======================================================================================================================================       
        
        
    elif choice1 == 2:
        print("모든이의 카드를 이동시킵니다.")
        while True:
            choice2 = int(input("방향을 정해주세요. : (오른쪽 : 1, 왼쪽 : 2를 눌러주세요."))#문자열로 받을지 숫자로 받을지는 추후에 정한다. 
            if choice2 > 2 or choice2<1:
                print("범위내의 숫자를 다시 입력해주세요.")
                continue
            else:
                break
                
        while True:
            num = int(input("카드를 얼마만큼 이동시킬지 정해주세요. (1~2)")) 
            if num > 2 or num<1:
                print("범위내의 숫자를 다시 입력해주세요.")
                continue
            else:
                break  
        
        if choice2 == 1:
            print("오른쪽을 선택하셨습니다.")
            if num ==1:
                print("오른쪽을 1칸씩 전부 이동시킵니다.")
                Print_Card = list(range(5))
                Print_Card[1] = Deck_Card[0]
                Print_Card[2] = Deck_Card[1]
                Print_Card[3] = Deck_Card[2]
                Print_Card[4] = Deck_Card[3]
                Print_Card[0] = Deck_Card[4]
        
            else:
                print("오른쪽으로 2칸씩 전부 이동시킵니다.")
                Print_Card = list(range(5))
                Print_Card[2] = Deck_Card[0]
                Print_Card[3] = Deck_Card[1]
                Print_Card[4] = Deck_Card[2]
                Print_Card[0] = Deck_Card[3]
                Print_Card[1] = Deck_Card[4]
            print(Print_Card)#최종 제거
            print("당신의 숫자는 {}입니다".format(Print_Card[M_Card - 1]))
            game_result = result(Print_Card[M_Card-1])
            print("==================결과=================")
            print("당신은 {}등입니다.".format(game_result))

        
        else:
            print("왼쪽을 선택하셨습니다.")
            if num ==1:
                print("왼쪽으로 전부 1칸씩 이동시킵니다.")
                Print_Card = list(range(5))
                Print_Card[4] = Deck_Card[0]
                Print_Card[0] = Deck_Card[1]
                Print_Card[1] = Deck_Card[2]
                Print_Card[2] = Deck_Card[3]
                Print_Card[3] = Deck_Card[4]

            else:
                print("왼쪽으로 전부 2칸씩 이동시킵니다.")
                Print_Card = list(range(5))
                Print_Card[3] = Deck_Card[0]
                Print_Card[4] = Deck_Card[1]
                Print_Card[0] = Deck_Card[2]
                Print_Card[1] = Deck_Card[3]
                Print_Card[2] = Deck_Card[4]    
            print(Print_Card)#최종 제거
            print("당신의 숫자는 {}입니다".format(Print_Card[M_Card - 1]))
            game_result = result(Print_Card[M_Card-1])
            print("==================결과======================")
            print("당신은 {}등입니다.".format(game_result))

    elif choice1 ==3:
        print("카드를 다시 섞습니다.")
        Deck_Card = np.random.choice(range(1,6),5,replace = False)
        print(Deck_Card)
        print("당신의 숫자는 {}입니다".format(Deck_Card[M_Card - 1]))
        game_result = result(Deck_Card[M_Card-1])
        print("==================결과======================")
        print("당신은 {}등입니다.".format(game_result))

    else:
        game_result = result(Deck_Card[M_Card-1])
        print("==================결과======================")
        print("당신은 {}등입니다.".format(game_result))

#==================================================================================================================================
else:
    C_Card = np.where(Deck_Card==RandNum)
    listA = list(C_Card)#위에 C_Card는 튜플이기 때문에 숫자를 출력할 수 없다 그래서 리스트형으로 형변환
    print("카드번호는")
    print(listA[0])
    #리스트로 출력하면 리스트 0번째가 몇번쨰 위치인지 나타내기때문에 listA[0]만 사용
    if listA[0] == 0:
        computer_Card = 1
    elif listA[0] == 1:
        computer_Card = 2
    elif listA[0] == 2:
        computer_Card = 3
    elif listA[0] == 3:
        computer_Card = 4
    elif listA[0] == 4:
        computer_Card = 5
    #배열로 0번쨰는 우리가 고를떄 1번째이기 때문에 if문 사용하여 몇번쨰인지 computer_Card에 대입
        
    computer_Num = Deck_Card[computer_Card-1]
    print("1.카드 번호{}".format(computer_Card))
    print("2.카드 숫자{}".format(computer_Num))
    
    print(Deck_Card)
    print("다른 플레이어가 옵션을 선택합니다.")
    print("============================================")
    print("1. 다른 플레이어와 카드를 교환하시겠습니까? ")
    print("2. 모든 플레이어의 카드를 바꾸겠습니까?")
    print("3. 판을 엎고 게임을 끝내시겠습니까? ")
    print("4. 게임을 끝내시겠습니까?")
    print("============================================")
    
    if computer_Num > 3:
        print("다른 플레이어가 4번을 선택하였습니다.")
        print("게임을 종료합니다.")
        print("당신의 카드 숫자는 {}입니다".format(Deck_Card[M_Card - 1]))
        game_result = result(Deck_Card[M_Card-1])
        print("==================결과======================")
        print("당신은 {}등입니다.".format(game_result))
        
    else:
        choice1 = random.randint(1,3)
        print(choice1) #최종에서 지우기

        if choice1 == 1:
            print("다른 플레이어가 1번을 선택하셨습니다. 다른 플레이어는 원하는 인원과 카드를 교환합니다.")
            print("다른 플레이어는 원하는 인원과 카드를 교환합니다.")
            print("방향을 정하시오: (오른쪽: 1, 왼쪽: 2)" ) #문자열로 받을지 숫자로 받을지는 추후에 정한다. 
            print("몇번째 인원과 바꿀건지 고르시오(1번째~2번째)")
            choice2 = random.randint(1,2)
            print(choice2)#애매
            num = random.randint(1,2)
            print(num)#애매
            
            if choice2 == 1:
                print("다른 플레이어가 오른쪽을 선택하셨습니다.")
                print("오른쪽 {}번째 인원과 카드를 교환합니다.".format(num))
                if(computer_Card + num > len(Deck_Card)):
                    Deck_Card[computer_Card-1], Deck_Card[computer_Card-1+ num-(len(Deck_Card))] = Deck_Card[computer_Card-1+ num-(len(Deck_Card))], Deck_Card[computer_Card-1] 
                else:
                    Deck_Card[computer_Card-1], Deck_Card[computer_Card-1 + num] = Deck_Card[computer_Card-1 + num], Deck_Card[computer_Card-1] 
                
                print(Deck_Card)
            else:
                print("다른 플레이어가 왼쪽으로 선택하셨습니다. ")
                print("왼쪽 {}번째 인원과 카드를 교환합니다.".format(num))
                Deck_Card[computer_Card], Deck_Card[computer_Card - num] = Deck_Card[computer_Card - num], Deck_Card[computer_Card] 
                print(Deck_Card)#최종 제거

            print("당신의 숫자는 {} 입니다".format(Deck_Card[M_Card-1]))
            game_result = result(Deck_Card[M_Card-1])
            print("==================결과======================")
            print("당신은 {}등입니다.".format(game_result))
        
        elif choice1 == 2:
            print("방향을 정하시오: (오른쪽: 1, 왼쪽: 2)")#문자열로 받을지 숫자로 받을지는 추후에 정한다.
            choice2 = random.randint(1,2)
            print("얼만큼 움직일지 정하시오. (1~2)") 
            num = random.randint(1,2)
            if choice2 == 1:
                print("다른 플레이어가 오른쪽을 선택하셨습니다.")
                if num ==1:
                    print("오른쪽으로 전부 1칸씩 옮기겠습니다.")
                    Print_Card = list(range(5))
                    Print_Card[1] = Deck_Card[0]
                    Print_Card[2] = Deck_Card[1]
                    Print_Card[3] = Deck_Card[2]
                    Print_Card[4] = Deck_Card[3]
                    Print_Card[0] = Deck_Card[4]
                    

                else:
                    print("오른쪽으로 전부 2칸씩 옮기겠습니다.")
                    Print_Card = list(range(5))
                    Print_Card[2] = Deck_Card[0]
                    Print_Card[3] = Deck_Card[1]
                    Print_Card[4] = Deck_Card[2]
                    Print_Card[0] = Deck_Card[3]
                    Print_Card[1] = Deck_Card[4]
                print(Print_Card)#최종 제거
                print("당신의 숫자는 {} 입니다".format(Print_Card[M_Card-1]))
                game_result = result(Print_Card[M_Card-1])
                print("==================결과======================")
                print("당신은 {}등입니다.".format(game_result))

            else:
                print("다른 플레이어가 왼쪽을 선택하셨습니다.")
                if num ==1:
                    print("왼쪽으로 1칸 옮기겠습니다.")
                    Print_Card = list(range(5))
                    Print_Card[4] = Deck_Card[0]
                    Print_Card[0] = Deck_Card[1]
                    Print_Card[1] = Deck_Card[2]
                    Print_Card[2] = Deck_Card[3]
                    Print_Card[3] = Deck_Card[4]

                else:
                    print("왼쪽으로 2칸 옮기겠습니다.")
                    Print_Card = list(range(5))
                    Print_Card[3] = Deck_Card[0]
                    Print_Card[4] = Deck_Card[1]
                    Print_Card[0] = Deck_Card[2]
                    Print_Card[1] = Deck_Card[3]
                    Print_Card[2] = Deck_Card[4]    
                print(Print_Card)#최종 제거
                print("당신의 숫자는 {} 입니다".format(Print_Card[M_Card-1]))
                game_result = result(Print_Card[M_Card-1])
                print("==================결과======================")
                print("당신은 {}등입니다.".format(game_result))

        else:
            print("다른 플레이어가 3번을 선택하셨습니다.")
            print("카드를 다시 섞습니다.")
            Deck_Card = np.random.choice(range(1,6),5,replace = False)
            print(Deck_Card)#최종 제거
            print("당신의 숫자는 {}입니다".format(Deck_Card[M_Card - 1]))
            game_result = result(Deck_Card[M_Card-1])#함수 불러오기
            print("==================결과======================")
            print("당신은 {}등입니다.".format(game_result))
    
    
 
