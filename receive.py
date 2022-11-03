
import socket, sys
from _thread import *
import data
sys.path.insert(0, '../data')
HOST = data.ip
PORT = 1000


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024).decode()
        if not data.startswith('['):
            if ' | ' in data:
                continue
            if(len(data.split(' : '))==1 and not "나가셨습니다" in data):
                print(f"{data}님이 입장하셨습니다")
                continue

            else :
                content = data.split(' : ')[1]
                print(data)#"recive : ",
            """if content.startswith("["):
                list1 = eval(content)
                if(list1[0] == )"""
start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')
while(1):
    pass
client_socket.close()