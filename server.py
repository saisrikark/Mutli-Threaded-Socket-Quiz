#!/usr/bin/env python3

from threading import Thread
import socket
import time

names = list()
answers = list()
questions = list()

MAX_NO_OF_PLAYERS = 100 #just for mentioning to listening socket
no_of_players = 0
quiz_start = False
quiz_end = False

HOST = '127.0.0.1'
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client_conn(client, addr, player_no):
    print("This is me")
    ques_no = 0
    name = client.recv(1024)
    names.append(name)
    while(not started_quiz):
        print("T")
        pass
    print("Hi there")
    while(ques_no < tot_no_of_questions):
        while(ques_no >= no_of_questions_entered):
            pass
        while(ques_no < no_of_questions_entered):
            print("This is a new question")
            t0 = time.time()
            client.send(question[ques_no])
            ans = client.recv(1024)
            t1 = time.time()
            answers.append((t1 - t0, player_no, t1 - t0, question_no, ans))
            ques_no += 1
        
    client.close()


print("Quiz Program started")

s.bind((HOST, PORT))
s.listen(MAX_NO_OF_PLAYERS)

while True:
    print("Waiting for players to join ...")
    conn, addr = s.accept()
    t = Thread(target = client_conn, args=(conn, addr, no_of_players+1))
    no_of_players += 1
    print(str(no_of_players) + " players have joined")
    print("Press Y(Yes) to wait for more players or N(No) to start the Quiz")
    choice = input()
    if(choice == "N"):
        break

started_quiz = True

print("Enter no of questions to be entered")
tot_no_of_questions = int(input())

no_of_questions_entered = 0
while(no_of_questions_entered < tot_no_of_questions):
    print("Enter Question no. " + str(no_of_questions_entered+1))
    question = input()
    questions.append(question)
    no_of_questions_entered += 1

ended_quiz = True
