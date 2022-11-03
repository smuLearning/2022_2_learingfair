import socket
from _thread import *
import data
import random,time
client_sockets = [] # 서버에 접속한 클라이언트 목록
userData = []
# 서버 IP 및 열어줄 포트
HOST = data.ip
PORT = 1000
#역할 리스트
roles = ["마피아","의사","시민","시민","시민","마담","군인","마피아"]


# 쓰레드에서 실행되는 코드입니다.
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            print(data.decode())
            # ' : '이 포함 안될 경우, "나가셨습니다"가 수신 데이터에 포함 안될 경우
            if len(data.decode().split(' : ')) == 1 and not "나가셨습니다" in data.decode():
                global userData
                #ip, 포트, 닉네임 저장
                userData.append([addr[0],addr[1],data.decode()])
                for client in client_sockets :
                    if client != client_socket :
                        client.send(data)
            #데이터가 존재 하지 않는 경우
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            #' : '가 포함되어 잇는 경우
            elif len(data.decode().split(' : ')) == 2:
                if data.decode().split(" : ")[1].startswith('!'):
                    #!킬 명령어가 들어온 경우
                    if '!킬 ' in data.decode().split(' : ')[1]:
                        target = data.decode().split('!킬 ')[1]
                        for client in client_sockets:
                            if client != client_socket :
                                client.send(f"kill | {target}".encode())
                        print(f"kill | {target}")
                    #!힐 명령어가 들어온 경우
                    elif '!힐 ' in data.decode().split(' : ')[1]:
                        target = data.decode().split('!힐 ')[1]
                        for client in client_sockets:
                            if client != client_socket :
                                client.send(f"heal | {target}".encode())
                        print(f"heal | {target}")
                    #!게임시작 명령어가 들어온 경우
                    elif data.decode().split(' : ')[1] == '!게임시작':
                        for client in client_sockets:
                            if client != client_socket :
                                client.send("공지 : 잠시 기다려주세요(역할은 입력에 공지됩니다)".encode())
                        try :
                            n = 0
                            for n in range(len(userData)):
                                userData[n][3] = 0
                        except:
                            pass
                        for i in range(len(userData)):
                            if userData[i][2] == data.decode().split(' : ')[0]:
                                #userData i번 3번째에 데이터가 있는 경우 
                                try:
                                    userData[i][3] = "진행자"
                                #userData i번 3번째에 데이터가 없 경우 
                                except:
                                    userData[i].append("진행자")
                        role = random.sample(roles[:len(userData)-1],len(userData)-1)
                        cnt = 0
                        for n in range(len(userData)):
                            #진행자를 제외한 나머지 랜덤 역할 부여
                            if len(userData[n]) == 4:
                                if userData[n][3] == "진행자":
                                    print(userData[i][2])
                                    pass
                            else:
                                try:
                                    userData[n][3] = role[cnt]
                                except:
                                    userData[n].append(role[cnt])
                                cnt+=1
                            for client in client_sockets:
                                #모든 클라이언트로 이름과 역할 전송
                                client.send(f"['{userData[n][2]}','{userData[n][3]}']".encode())
                                time.sleep(0.5)
                else:
                    print('>> Received from ' + addr[0], ':', addr[1], data.decode())

                # 서버에 접속한 클라이언트들에게 채팅 보내기
                # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
                    for client in client_sockets :
                        if client != client_socket :
                            client.send(data)
        #나간 사람 나갔다고 표시하기
        except ConnectionResetError as e:
            num = None
            for i in range(len(userData)):
                if userData[i][1] == addr[1]:
                    num = i
                    break
            if num != None:
                for client in client_sockets :
                    if client != client_socket:
                        client.send(f"공지 : {userData[num][2]}님이 나가셨습니다".encode())
                #userData = [user for user in userData if user[2] != userData[num][2]]         
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))
    
    client_socket.close()

# 서버 소켓 생성
print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))
        
except Exception as e :
    print ('에러는? : ',e)

finally:
    server_socket.close()




