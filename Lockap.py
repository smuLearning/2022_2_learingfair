#기본 공통코드

import tkinter #파이썬에서 GUI를 다루기 위해 tkinter모듈을 불러옵니다

root = tkinter.Tk() #창 요소 생성
root.title("Lock__A+조 프로젝트 과제") #창 제목 설정
canvas = tkinter.Canvas(root, width=800, height=600) #캔버스 크기 설정
canvas.pack() #캔버스 배치

#--------------------------------------------------------------------------------------------------S#1~3 (조유진)


start_background = tkinter.PhotoImage(file = "images/main_image.png") #이미지 설정 코드
label1 = tkinter.Label(root, image = start_background) #라벨에 이미지 적용
label1.place(x = 0, y = 0) #라벨 배치


print("\n게임은 tkinter창으로 진행됩니다. 창을 띄우고 진행해주세요.\n\n시작하시려면 화면의 '시작'을, 플레이 방법을 보시려면 '게임방법'을 눌러주세요.\n")


num = 0 #num변수 초기화 (리스트에서 사용할 변수)


def button_start_click():  #버튼 클릭시 함수 설정
    button_start


                 #start 버튼을 누르고 대화창 1-1을 로드합니다.
    global dialog1
    dialog1 = tkinter.PhotoImage(file = "images/1-1.png") #대화창1을 선언합니다.
    label1.config(image = dialog1) #위에서 선언했었던 label_startbg에 있는 이미지를 1-1.png로 전환합니다.
    label1.place(x = 0, y = 0) #이미지를 재배치합니다. 

    
    button_how.place_forget()
    button_start.place_forget()
    button_start_back.place(x=650, y=50)
    button_next.place(x=660, y=520)

    
button_start = tkinter.Button(text="시작", font=("Time New Roman", 16), height = 2, width = 15, command = button_start_click)
button_start.place(x=320, y=350)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def button_next_click():
    button_next

    global num
    global next_image
    num = num + 1     #num 증가
    next_img = py_Img[num] #리스트에서 이미지 불러오기
    label1.config(image = next_img) #label을 이용해 이미지 불러오기
    label1.place(x = 0, y = 0)
    
    if (num > 7): 
        button_s_4.place(x=650, y=520)
        button_next.place_forget()

    if (num == 1):
        button_forward.place(x=20, y=520)

    
button_next = tkinter.Button(text=">>", font=("Time New Roman", 16), height = 2, width = 10, command = button_next_click)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def button_forward_click():
    button_forward

    global num
    global forward_image #이전으로 가기
    num = num - 1
    forward_image = py_Img[num] #리스트에서 이미지 불러오기
    label1.config(image = forward_image) #label을 이용해 이미지 불러오기
    label1.place(x = 0, y = 0)

    if (num < 2):
        button_s_4.place_forget()

    if (num == 0):
        button_forward.place_forget()


button_forward = tkinter.Button(text="<<", font=("Time New Roman", 16), height = 2, width = 10, command = button_forward_click)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def button_how_click():
    
    button_start.place_forget()
    button_how.place_forget()
    button_how_back.place(x=650, y=50)

    global how1                              # 게임방법 이미지를 불러오기
    how1 = tkinter.PhotoImage(file = "images/how.png")
    label1.config(image = how1)
    label1.place(x = 0, y = 0)


button_how = tkinter.Button(text="게임 방법", font=("Time New Roman", 16), height = 2, width = 15, command = button_how_click)
button_how.place(x=320, y=420)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def button_start_back_click():
    button_start.place(x=320, y=350)
    button_how.place(x=320, y=420)
    button_start_back.place_forget()
    button_next.place_forget()
    button_forward.place_forget()

    global num
    num = 0

    if (num == 0):
        button_s_4.place_forget()
    
    global startbg                             # 메인 로고 이미지를 다시 불러오기
    startbg = tkinter.PhotoImage(file = "images/main_image.png")
    label1.config(image = startbg)
    label1.place(x = 0, y = 0)


button_start_back = tkinter.Button(text="돌아가기", font=("Time New Roman", 16), height = 2, width = 10,
                                   command = button_start_back_click)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def button_how_back_click():
    button_how.place(x=320, y=420)
    button_start.place(x=320, y=350)
    button_how_back.place_forget()
    button_next.place_forget()
    button_forward.place_forget()

    global num
    num = 0
    
    if (num == 0):
        button_s_4.place_forget()

    global startbg                             # 메인 로고 이미지를 다시 불러오기
    startbg = tkinter.PhotoImage(file = "images/main_image.png")
    label1.config(image = startbg)
    label1.place(x = 0, y = 0)
    
button_how_back = tkinter.Button(text="돌아가기", font=("Time New Roman", 16), height = 2, width = 10,
                                 command = button_how_back_click)


#--------------------------------------------------------------------------------------------------S#4 (권수빈))

def s_4():                                   #S#4로 넘어가는 코드
    
    global classroom_back
    classroom_back = tkinter.PhotoImage(file = "images/class_back.png")
    label1.config(image = classroom_back)
    label1.place(x = 0, y = 0)
    
    desk_school.place(x = 20, y = 310)
    desk_school['state']= 'disabled'
    clean_box_school.place(x = 300, y = 250)
    locker_school.place(x = 700, y = 200)
    com_school.place(x = 250, y = 150)
    com_school['state']= 'disabled'
    bord_school.place(x = 500, y = 220)

    button_s_4.place_forget()
    button_start_back.place_forget()
    button_next.place_forget()
    button_forward.place_forget()

    print("<학교 교실>")
    print("정진욱: 아... 뭘 찾으라는 거야. 지가 누군지 내가 어떻게 알아.")
    print("정진욱: 우리 고등학교 교실이랑 비슷하게 생겼네. 그때... 내가 끝번이었으니까...30번이었나?")
    print("교실처럼 꾸며진 방안에 [책상,의자,사물함,청소도구함,컴퓨터]이/가 있다.")
    
button_s_4 = tkinter.Button(text = "교실로 이동", font=("Time New Roman", 16), height = 2, width = 10, command = s_4)


i = 0 #i값 초기화(책상, 사물함, 청소도구함, 컴퓨터를 볼 때마다 1씩 추가)
classback = 0


    
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def desk_school_click(): #책상버튼함수
    print("살펴볼 책상의 번호를 선택하시오")
        
    def desk_30_school_click(): #30번 책상
        print("다른 사람의 것으로 보이는 과제 노트가 있다.")
        print("표지에 적힌 글자는 거의 지워져 있다. 검게 칠해진 사이로 '18번'이라는 글자가 보인다.")
        print("정진욱: 이 노트는 내 껀 아닌 것 같은데... 누군지 몰라도 과제 열심히 했네.")

        def desk_30_school_click_close_click():
            locker_school['state']= 'normal'
            clean_box_school['state']= 'normal'
            com_school['state']= 'normal'
            desk_school_close.place_forget()  
            
            global i #전역 변수로 변수 i를 설정합니다. 
            i = i + 1 #i에 1을 늘립니다. (책상, 청소도구함, 사물함, 컴퓨터를 모두 보았을 때 i는 4가 됩니다.)
            if (i == 4): #if문을 사용하여 만약 i가 4일 때 칠판 버튼을 활성화합니다.
                bord_school['state']= 'normal'
        
        desk_30_school.place_forget()


        desk_school_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = desk_30_school_click_close_click) #교과서 닫기 버튼 생성
        desk_school_close.place(x=700, y=100)


    desk_30_school = tkinter.Button(text="30번 책상", font=("Time New Roman", 16), command = desk_30_school_click)
    desk_30_school.place(x=460,y=550)


    def desk_18_school_click(): #18번 책상
        print("책상 중간에 피가 떨어져 있다. 점성이나 뿌려진 모양으로 볼 때 코피인 것 같다.")
        print("정진욱: 웬 코피가 이렇게...")
        
        def desk_18_school_click_close_click():
            locker_school['state']= 'normal'
            clean_box_school['state']= 'normal'
            com_school['state']= 'normal'
            desk_school_close.place_forget()  


        desk_18_school.place_forget()


        desk_school_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = desk_18_school_click_close_click) #교과서 닫기 버튼 생성
        desk_school_close.place(x=700, y=100)


    desk_18_school = tkinter.Button(text="18번 책상", font=("Time New Roman", 16), command = desk_18_school_click)
    desk_18_school.place(x=250,y=350)

    locker_school['state']= 'disabled'
    clean_box_school['state']= 'disabled'
    com_school['state']= 'disabled'

    desk_school.place_forget()

    
desk_school = tkinter.Button(text="책상", font=("Time New Roman",16), command = desk_school_click) #책상버튼 배치
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def clean_box_school_click(): #청소도구함 버튼 생성
    print("부러진 빗자루 두어개와 대걸레 따위가 들어있다.")
    print("정진욱: 와... 이것까지 비슷하냐...나도 고딩 때 빗자루 휘두르다가 몇개 부러뜨렸는데.")
    print("대걸레를 들어올리자 아래쪽에 놓여 있던 것이 드러난다.")


    global classback
    classback = classback + 1
    if (classback == 2):
        desk_school['state']= 'normal'
        com_school['state']= 'normal'

    
    def clean_box_school_click_close_click():
        locker_school['state']= 'normal'
        desk_school['state']= 'normal'
        com_school['state']= 'normal'
        clean_box_school_click_close.place_forget()

        global i #전역 변수로 변수 i를 설정합니다. 
        i = i + 1 #i에 1을 늘립니다. (책상, 청소도구함, 사물함, 컴퓨터를 모두 보았을 때 i는 4가 됩니다.)
        if (i == 4): #if문을 사용하여 만약 i가 4일 때 칠판 버튼을 활성화합니다.
            bord_school['state']= 'normal'

        global classroom
        classroom = tkinter.PhotoImage(file = "images/class.png")
        label1.config(image = classroom)
        label1.place(x = 0, y = 0)


    clean_box_school_click_close = tkinter.Button(text="닫기", font=("Time New Roman",16), command = clean_box_school_click_close_click)
    clean_box_school_click_close.place(x=700,y=100)

    locker_school['state']= 'disabled'
    desk_school['state']= 'disabled'
    com_school['state']= 'disabled'

    clean_box_school.place_forget()


clean_box_school = tkinter.Button(text="청소도구함", font=("Time New Roman",16), command = clean_box_school_click) 
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def locker_school_click(): #사물함 버튼 생성
    print("살펴볼 사물함의 번호를 선택하시오.")


    global classback
    classback = classback + 1
    if (classback == 2):
        desk_school['state']= 'normal'
        com_school['state']= 'normal'

        
    global classroom_back
    classroom_back = tkinter.PhotoImage(file = "images/class_back.png")
    label1.config(image = classroom_back)
    label1.place(x = 0, y = 0)
    
    global i #전역 변수로 변수 i를 설정합니다.
    i = i + 1 #i에 1을 늘립니다. (책상, 청소도구함, 사물함, 컴퓨터를 모두 보았을 때 i는 4가 됩니다.)
    if (i == 4): #if문을 사용하여 만약 i가 4일 때 칠판 버튼을 활성화합니다.
        bord_school['state']= 'normal'

    
    def locker_30_school_click(): #30번 사물함
        print("대충 던져진 책 몇 권, 흙이 묻은 축구화와 축구공이 놓여있다.")
        print("던져진 책들 사이에 부러진 열쇠가 있다.")
        
        def locker_30_school_click_close_click():
            clean_box_school['state']= 'normal'

            locker_school_close.place_forget()

            locker_18_school['state'] = 'normal'

        locker_30_school.place_forget()

        locker_school_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = locker_30_school_click_close_click) #교과서 닫기 버튼 생성
        locker_school_close.place(x=700, y=100)


    locker_30_school = tkinter.Button(text="30번사물함", font=("Time New Roman", 16), command = locker_30_school_click)
    locker_30_school.place(x=600,y=300)

    def locker_18_school_click():
        print("자물쇠가 달린 수첩과 구겨지고 찢겨있지만 잘 정돈되어 꽂혀있는 교과서들이 있다.")

        def locker_18_school_click_close_click(): #18번 사물함
            clean_box_school['state']= 'normal'
            
            locker_school_close.place_forget()


        locker_18_school.place_forget()

        locker_school_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = locker_18_school_click_close_click) #교과서 닫기 버튼 생성
        locker_school_close.place(x=700, y=100)


    locker_18_school = tkinter.Button(text="18번 사물함", font=("Time New Roman", 16), command = locker_18_school_click)
    locker_18_school['state'] = 'disabled'
    locker_18_school.place(x=450,y=150)

    clean_box_school['state']= 'disabled'
    desk_school['state']= 'disabled'
    com_school['state']= 'disabled'

    locker_school.place_forget()


locker_school = tkinter.Button(text="사물함", font=("Time New Roman",16), command = locker_school_click)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
def com_school_click(): #컴퓨터 버튼 생성
    print("10년 전에나 썼을 법한 오래된 컴퓨터이다.")
    

    def com_school_click_close_click():
        clean_box_school['state']= 'normal'
        desk_school['state']= 'normal'
        locker_school['state']= 'normal'

        global i #전역 변수로 변수 i를 설정합니다. 
        i = i + 1 #i에 1을 늘립니다. (책상, 청소도구함, 사물함, 컴퓨터를 모두 보았을 때 i는 4가 됩니다.)
        if (i == 4): #if문을 사용하여 만약 i가 4일 때 칠판 버튼을 활성화합니다.
            bord_school['state']= 'normal'
        
        com_click_close.place_forget()  #닫기 버튼을 눌렀을 때 닫기 버튼이 사라지는 함수입니다.


    com_click_close = tkinter.Button(text="닫기", font=("Time New Roman",16), command = com_school_click_close_click)
    com_click_close.place(x=700,y=100)

    clean_box_school['state']= 'disabled'
    desk_school['state']= 'disabled'
    locker_school['state']= 'disabled'

    com_school.place_forget()

com_school = tkinter.Button(text="컴퓨터", font=("Time New Roman",16), command = com_school_click)



#--------------------------------------------------------------------------------------------------S#5 (최우혁)
def bord_school_click():
    print('칠판에 무언가 적혀있었다.\n')
    print('<가정집처럼 꾸며진 장소>')
    print('교실 앞문을 열고 나가니 어떤 가정집에 도착했다')
    print('정진욱 : 낯익은 풍경인데...')
    print('가정집처럼 꾸며진 방 안에 [침대, 책상, 서랍, 옷장]이/가 있다.')
    
    global home
    home = tkinter.PhotoImage(file = "images/home_background.png")
    label1.config(image = home)
    label1.place(x = 0, y = 0)

    bord_school.place_forget()  
    bed_house_2.place(x = 375, y = 350)


bord_school = tkinter.Button(text="칠판", font=("Time New Roman",16), command = bord_school_click) #비활성화 상태의 칠판 버튼 배치

bord_school['state']= 'disabled'

key = 0 #열쇠 값 초기화
j = 0 #j값 초기화(책상, 침대, 수납장, 의자, 옷장을 볼 때마다 1씩 추가됩니다.)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#침대 버튼 함수
def bed_house_2_click():
    print('침대에서 [담배](특정 디자인)를 발견했다.')
    
    global j #전역 변수로 변수 i를 설정합니다. 최종 문 버튼을 생성하기 위한 조건
    j = j + 1 #i에 1을 늘립니다.

    global tabaco              #담배 이미지를 로드
    tabaco = tkinter.PhotoImage(file = "images/tabaco.png")
    label1.config(image = tabaco)
    label1.place(x = 0, y = 0)

    dask_house_2.place_forget() #책상 버튼 삭제 (이미지를 로드 했을 때 버튼이 화면을 가리는 것을 방지)
    closet_house_2.place_forget() #옷장 버튼 삭제
    drawer_house_2.place_forget() #수납장 버튼 삭제
    chair_house_2.place_forget() #의자 버튼 삭제
    
    def bed_house_2_click_close_click():#닫기 버튼 함수

        global home       #로드된 담배 이미지를 닫고 다시 메인배경을 로드
        home = tkinter.PhotoImage(file = "images/home_background.png")
        label1.config(image = home) 
        label1.place(x = 0, y = 0)

        
        #이미지를 로드했을 때 삭제했던 버튼을 다시 불러옴
        dask_house_2.place(x= 610, y=300)

        bed_house_2_click_close.place_forget() #닫기 버튼 삭제
        
    bed_house_2_click_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = bed_house_2_click_close_click) #담배 이미지 닫기 버튼 생성
    bed_house_2_click_close.place(x=700, y=100)
    
    bed_house_2.place_forget() #침대 버튼 삭제
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#책상 버튼 함수
def dask_house_2_click():
    print('책상에 [교과서, 일기장, 소설책]이 있다. 무엇을 살펴볼까?')
    
    global j #전역 변수로 변수 i를 설정합니다.
    j = j + 1 #i에 1을 늘립니다.

    global dask_on   #책상 위의 책들 이미
    dask_on = tkinter.PhotoImage(file = "images/dask_on.png")
    label1.config(image = dask_on)
    label1.place(x = 0, y = 0)
    
    def textbook_click():                                                    #교과서 버튼 클릭 함수
        print('고등학교 3학년의 교과서가 쌓여있다.')
    
        global textbook_img   #책상 위 교과서 이미지
        textbook_img = tkinter.PhotoImage(file = "images/textbook.png")
        label1.config(image = textbook_img)
        label1.place(x = 0, y = 0)

        def textbook_close_click():

            global home       #로드된 교과서 이미지를 닫고 다시 메인배경을 로드
            home = tkinter.PhotoImage(file = "images/home_background.png")
            label1.config(image = home) 
            label1.place(x = 0, y = 0)
            
            closet_house_2.place(x= 125, y=300) #옷장 버튼 배치

            textbook_close.place_forget() #교과서 닫기 버튼 삭제
            
        textbook_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = textbook_close_click) #교과서 닫기 버튼 생성
        textbook_close.place(x=700, y=100)
        
        textbook.place_forget() #교과서 버튼 삭제(점수 중복 획득 방지)
        diary.place_forget() #일기장 버튼 삭제(점수 중복 획득 방지)
        novel.place_forget() #소설책 버튼 삭제(점수 중복 획득 방지)
        
    def diary_click():                                                       #일기장 버튼 클릭 함수
        print('빼곡하게 글이 적힌 두툼한 노트. 거의 매일 적은 듯하다.')
        global diary_1    #일기 1페이지
        diary_1 = tkinter.PhotoImage(file = "images/diary_1.png")
        label1.config(image = diary_1)
        label1.place(x = 0, y = 0)
        
        def pass_page_click1():

            global diary_2    #일기 2페이지
            diary_2 = tkinter.PhotoImage(file = "images/diary_2.png")
            label1.config(image = diary_2)
            label1.place(x = 0, y = 0)

            pass_page1.place_forget()
            
            def pass_page_click2():

                global diary_3    #일기 1페이지
                diary_3 = tkinter.PhotoImage(file = "images/diary_last.png")
                label1.config(image = diary_3)
                label1.place(x = 0, y = 0)
        
                global key    #열쇠 흭득
                key = key + 1

                pass_page2.place_forget()

            pass_page2 = tkinter.Button(text="뒷장 보기", font=("Time New Roman", 16), command = pass_page_click2) #일기장의 뒷면2으로 넘기는 버튼 생성
            pass_page2.place(x=700, y=500)
        
            def close_diary_click():

                global home       #로드된 일기장 이미지를 닫고 다시 메인배경을 로드
                home = tkinter.PhotoImage(file = "images/home_background.png")
                label1.config(image = home) 
                label1.place(x = 0, y = 0)

                closet_house_2.place(x= 125, y=300) #옷장 버튼 배치
            
                close_diary.place_forget() #일기장 닫기 버튼 삭제
                
                
                pass_page2.place_forget() #넘기기 버튼 삭제
            
            close_diary = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = close_diary_click) #일기장 닫기 버튼 생성
            close_diary.place(x=700, y=100)
            
        pass_page1 = tkinter.Button(text="뒷장 보기", font=("Time New Roman", 16), command = pass_page_click1) #일기장의 뒷면1으로 넘기는 버튼 생성
        pass_page1.place(x=700, y=500)

        

        
        textbook.place_forget() #교과서 버튼 삭제
        diary.place_forget() #일기장 버튼 삭제
        novel.place_forget() #소설책 버튼 삭제
        
    def novel_click():                                                       #소설책 버튼 클릭 함수
        print('‘우리는 왜 사람을 미워할까’라는 제목의 책이 놓여 있다.')
        print('[동그란 얼굴... 하얀 피부...] 라고 적혀있는 부분에 밑줄이 그어져있다.')
        
        global novel_img    #소설책 불러오기
        novel_img = tkinter.PhotoImage(file = "images/novel.png")
        label1.config(image = novel_img)
        label1.place(x = 0, y = 0)
        
        def close_novel_click():

            global home       #로드된 소설 이미지를 닫고 다시 메인배경을 로드
            home = tkinter.PhotoImage(file = "images/home_background.png")
            label1.config(image = home) 
            label1.place(x = 0, y = 0)

            closet_house_2.place(x= 125, y=300) #옷장 버튼 배치
            
            close_novel.place_forget()#소설 닫기 버튼 삭제
            
        close_novel = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = close_novel_click) #소설책 닫기 버튼 생성
        close_novel.place(x=700, y=100)

        textbook.place_forget() #교과서 버튼 삭제
        diary.place_forget() #일기장 버튼 삭제
        novel.place_forget() #소설책 버튼 삭제

    
    #교과서,일기장, 소설책 버튼 생성
    textbook = tkinter.Button(text="교과서", font=("Time New Roman", 16), command = textbook_click)
    textbook.place(x=400, y=375)
    diary = tkinter.Button(text="일기장", font=("Time New Roman", 16),command = diary_click)
    diary.place(x=500, y=375)
    novel = tkinter.Button(text="소설책", font=("Time New Roman", 16), command = novel_click)
    novel.place(x=620, y=375)


    dask_house_2.place_forget() #책상 버튼 삭제
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#옷장 버튼 함수
def closet_house_2_click():
    print('정진욱 : 표준 체형인 내 옷보다 품이 훨씬 크네.')
    
    global closet_img    #옷장 속의 옷 불러오기
    closet_img = tkinter.PhotoImage(file = "images/closet_in.png")
    label1.config(image = closet_img)
    label1.place(x = 0, y = 0)

    global j #전역 변수로 변수 i를 설정합니다. 
    j = j + 1 #i에 1을 늘립니다.
        
    dask_house_2.place_forget() #책상 버튼 삭제 (이미지를 로드 했을 때 버튼이 화면을 가리는 것을 방지)
    drawer_house_2.place_forget() #수납장 버튼 삭제
    chair_house_2.place_forget() #의자 버튼 삭제
    bed_house_2.place_forget() #침대 버튼 삭제
    
    def closet_image_close_click():

        global home       #로드된 소설 이미지를 닫고 다시 메인배경을 로드
        home = tkinter.PhotoImage(file = "images/home_background.png")
        label1.config(image = home) 
        label1.place(x = 0, y = 0)
        
       
        drawer_house_2.place(x= 500, y=400)#수납장 버튼 생성
        
        closet_image_close.place_forget()#닫기 버튼 삭제
        
    

    closet_image_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = closet_image_close_click) #옷 이미지 닫기 버튼 생성
    closet_image_close.place(x=700, y=100)

    
    closet_house_2 .place_forget() #옷장 버튼 삭제
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#수납장 버튼 함수
def drawer_house_2_click():
    print('수납장 위에 진단서가 놓여 있다.')
    
    global diagnosis_img       #수납장 속 진단서 로드
    diagnosis_img = tkinter.PhotoImage(file = "images/diagnosis.png")
    label1.config(image = diagnosis_img) 
    label1.place(x = 0, y = 0)
    

    global j #전역 변수로 변수 i를 설정합니다. 
    j = j + 1 #i에 1을 늘립니다. 
        
    def diagnosis_image_close_click():
        print('방으로 들어오기 전 보았던 의자를 자세히 확인한다')
        
        global home       #로드된 소설 이미지를 닫고 다시 메인배경을 로드
        home = tkinter.PhotoImage(file = "images/home_background.png")
        label1.config(image = home) 
        label1.place(x = 0, y = 0)

        chair_house_2.place(x= 550, y=400) #의자 버튼 생성

        diagnosis_image_close.place_forget()#닫기 버튼 삭제

    diagnosis_image_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = diagnosis_image_close_click) #진단서 이미지 닫기 버튼 생성
    diagnosis_image_close.place(x=700, y=100)

    
    drawer_house_2.place_forget() #수납장 버튼 삭제
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#의자 버튼 함수
def chair_house_2_click():
    print('의자에 피가 묻은 교복 와이셔츠가 있다.')
    
    global shirts_img    #일기 1페이지
    shirts_img = tkinter.PhotoImage(file = "images/shirts.png")
    label1.config(image = shirts_img)
    label1.place(x = 0, y = 0)

    global j #전역 변수로 변수 i를 설정합니다. 
    j = j + 1 #i에 1을 늘립니다.
    
    if (j == 5): #if문을 사용하여 만약 i가 5일 때 문 버튼을 생성합니다.
        door_house_2.place(x = 400, y = 300)
        door_house_2['state']= 'disabled' #문 버튼을 잠시 비활성화
        
    def shirts_image_close_click():

        door_house_2['state'] = 'normal' #문 버튼 활성화
        
        global closed
        closed = tkinter.PhotoImage(file = "images/door.png")
        label1.config(image = closed) 
        label1.place(x = 0, y = 0)

        shirts_image_close.place_forget()#닫기 버튼 삭제

    shirts_image_close = tkinter.Button(text="닫기", font=("Time New Roman", 16), command = shirts_image_close_click) #진단서 이미지 닫기 버튼 생성
    shirts_image_close.place(x=700, y=100)
    
    chair_house_2.place_forget() #의자 버튼 삭제(점수 중복 획득 방지)
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#문버튼 함수
def door_house_2_click():

    global key 
    
    if (key == 1):         #만약 열쇠를 가지고 있다면 문을 열고 다음 장면으로

        print('닫혀있는 문이다. 아까 일기장을 확인하며 보았던 열쇠를 사용해보자.')
        print('문이 열렸다!')
        print('문을 열자 3명의 남성이 있다.')
        print('이 중 한명이 날 이곳으로 부른 범인일 것이다.')
        
        global homend
        homend = tkinter.PhotoImage(file = "images/3people.png") #사람3 이미지 불러오기 *****S#6으로 이어지는 코드
        label1.config(image = homend)
        label1.place(x = 0, y = 0)

        checkbutton_A.place(x = 100, y = 100) #위치지정
        checkbutton_B.place(x = 350, y = 100)
        checkbutton_C.place(x = 600, y = 100)
        
        
        print(key) #(임시)삭제 예정
        
        door_house_2.place_forget() #문버튼 삭제
        
    else:                  #열쇠를 가지고 있지 않다면 게임오버

        print('문이 열리지 않는다.열쇠가 필요한 듯 하다.')
        global game_over #게임오버 이미지 불러오기
        game_over = tkinter.PhotoImage(file = "images/game_over.png")
        label1.config(image = game_over)
        label1.place(x = 0, y = 0)

        door_house_2.place_forget() #문버튼삭제
        

#버튼 배치
bed_house_2 = tkinter.Button(text="침대", font=("Time New Roman", 16), command = bed_house_2_click)
dask_house_2 = tkinter.Button(text="책상", font=("Time New Roman", 16), command = dask_house_2_click) 
closet_house_2 = tkinter.Button(text="옷장", font=("Time New Roman", 16), command = closet_house_2_click)
drawer_house_2 = tkinter.Button(text="수납장", font=("Time New Roman", 16), command = drawer_house_2_click)
chair_house_2 = tkinter.Button(text="의자", font=("Time New Roman", 16), command = chair_house_2_click)
door_house_2 = tkinter.Button(text="열기", font=("Time New Roman", 16), command = door_house_2_click)

#--------------------------------------------------------------------------------------------------S#6,7 (김가연)

def click():
    if var_B.get() == True:
        print("정답!")

        global success
        success = tkinter.PhotoImage(file="images/success.png")
        label1 = tkinter.Label(root, image = success)
        label1.place(x = 0 , y = 0)

        for i in range (0, 100, 1):
            print("내 복수가 여기서 끝날 거라고 생각해?")
            
    elif var_A.get() == True:
        print("범인을 찾지 못하였습니다. GAME OVER")

        global gameover
        gameover = tkinter.PhotoImage(file="images/gameover.png")
        label1 = tkinter.Label(root, image = gameover)
        label1.place(x = 0 , y = 0)


    elif var_C.get() == True:
        print("범인을 찾지 못하였습니다. GAME OVER")
         
        gameover = tkinter.PhotoImage(file="images/gameover.png")
        label1 = tkinter.Label(root, image = gameover)
        label1.place(x = 0 , y = 0)


var_A = tkinter.BooleanVar()
var_A.set(False)

var_B = tkinter.BooleanVar()
var_B.set(False)

var_C = tkinter.BooleanVar()
var_C.set(False)



checkbutton_A = tkinter.Checkbutton (text = "용의자 A",variable = var_A , command=click) #체크박스 생성
checkbutton_B = tkinter.Checkbutton (text = "용의자 B",variable = var_B , command=click)
checkbutton_C = tkinter.Checkbutton (text = "용의자 C",variable = var_C , command=click)


py_Img = [tkinter.PhotoImage(file="images/1-1.png"),tkinter.PhotoImage(file="images/1-2.png"), tkinter.PhotoImage(file="images/1-3.png"),tkinter.PhotoImage(file="images/1-4.png"),tkinter.PhotoImage(file="images/1-5.png"),tkinter.PhotoImage(file="images/1-6.png"),tkinter.PhotoImage(file="images/1-7.png"),tkinter.PhotoImage(file="images/1-8.png"),tkinter.PhotoImage(file="images/1-9.png")]

root.mainloop()




