#!/usr/bin/env python3

import socket

from threading import Thread
from os import getpid

PID=getpid()
TCP_PORT=6000
TCP_HOST='127.0.0.1'
QUESTION_COUNTER=0
SEND_STRING=""

#Creating socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setblocking(True)
#Initial data sent to register as a client
NAME=input("Enter your name :")

'''
def check_connection():
    while(True):
        try:
            #bytes(mystring, 'utf-8')
            SEND_STRING="Check connection"+" "+NAME
            s.send(bytes(SEND_STRING,'utf-8'))
            break
        except:
            #print("Trying to establish connection again.")
            try:
                s.connect((TCP_HOST,TCP_PORT))
                break
            except:
                pass
                #print("Not connecting trying again")
'''

def establish_connection():
    while(True):
        try:
            print("Established")
            s.connect((TCP_HOST,TCP_PORT))
            break
        except:
            print("Connection not established")
#In case you want some timeout ask server to send
#t=s.recv(BUFFERSIZE)

establish_connection()
s.sendall(NAME.encode())
s.recv(1024)
print("Hello this is me")
while(QUESTION_COUNTER<3):
    #check_connection()
    q=s.recv(1024)
    #print("My dear friends")
    s.sendall("why the hell are you doing?".encode())
    print(q.decode())
    #QUESTION_COUNTER+=1

s.close()
