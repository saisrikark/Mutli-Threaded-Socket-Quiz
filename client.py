#!/usr/bin/env python3


from threading import Thread
import socket
from os import getpid

PID=getpid()
TCP_PORT=6000
TCP_HOST='127.0.0.1'
BUFFERSIZE=1000
QUESTION_COUNTER=0
SEND_STRING=""

#Creating socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Initial data sent to register as a client
NAME=input("Enter your name :")

def check_connection():
    while(True):
        try:
            #bytes(mystring, 'utf-8')
            SEND_STRING="Check connection"+" "+NAME
            s.send(bytes(SEND_STRING,'utf-8'))
            break
        except:
            print("Trying to establish connection again.")
            s.connect((TCP_HOST,TCP_PORT))

def establish_connection():
	s.connect((TCP_HOST,TCP_PORT))

#In case you want some timeout ask server to send
#t=s.recv(BUFFERSIZE)

establish_connection()

while(QUESTION_COUNTER<3):
    check_connection()
    q=s.recv(BUFFERSIZE)
    print(q.decode('utf-8'))
    QUESTION_COUNTER+=1

s.close()
