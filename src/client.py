#!/usr/bin/env python3

import socket
import time
from threading import Thread
from os import getpid

PID=getpid()
TCP_PORT=6000
TCP_HOST='192.168.43.143'
QUESTION_COUNTER=0
SEND_STRING=""
answer=''

#Creating socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setblocking(True)
#Initial data sent to register as a client
NAME=input("Enter your name :")

def establish_connection():
    while(True):
        try:
            print("Established")
            s.connect((TCP_HOST,TCP_PORT))
            break
        except:
            print("Connection not established")
            time.sleep(1)

establish_connection()
s.sendall(NAME.encode())

NO_OF_QUESTIONS = s.recv(1024)
NO_OF_QUESTIONS = int(NO_OF_QUESTIONS.decode())

print("The no of questions in this Test is " + str(NO_OF_QUESTIONS))
print("Hello this is me")
while(QUESTION_COUNTER < NO_OF_QUESTIONS):
    q=s.recv(1024)
    print(q.decode())# + "My dear friends")
    answer = input()
    s.sendall(answer.encode())
    QUESTION_COUNTER+=1

s.close()
