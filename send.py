import socket, sys, os
from _thread import *
sys.path.insert(0, '../data')
import data,time
HOST = data.ip
PORT = 1000
role = ""

nick = input('닉네임을 정해주세요 : ')
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(nick.encode())
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024).decode()
        if data:
            if data.startswith("["):
                #print(data)
                list1 = eval(data)
                if list1[0] == nick:
                    global role
                    role = list1[1]
                    print(f"당신의 역할은 {role}입니다")
            elif "kill" in data:
                if role == "진행자":
                    print(data.split(" | ")[1] + "님이 지목 당하셨습니다.")
            elif "heal" in data:
                if role == "진행자":
                    print(data.split(" | ")[1] + "님을 치료 했습니다")
                
start_new_thread(recv_data, (client_socket,))

while True:
    time.sleep(0.2)
    if role == "진행자":
        message = nick + "(진행자) : " + input('입력해주세요 : ')
    elif role != "":
        message = nick + " : " + input(f'입력해주세요({role}) : ')
    else :message = nick + " : " + input(f'입력해주세요 : ')
    if "!킬" in message:
        if role != "마피아":
            continue
    if "!힐" in message:
        if role != "의사":
            continue
    
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())
    #os.system("cls")


client_socket.close()