#!/usr/bin/env python3

from threading import Thread
import socket

names = list()
answers = list()
questions = list()
answers = list()

MAX_NO_OF_PLAYERS = 100 #just for mentioning to listening socket
no_of_players = 0
quiz_start = False
quiz_end = False

HOST = '192.168.43.55'
PORT = 6000

started_quiz = False
TOT_NO_OF_QUESTIONS = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(True)

def client_conn(client, addr, player_no):
    print("Thread forked of for new client")
    ques_no = 0
    anstot = 0
    name = client.recv(1024)
    #receiving name from client
    print(name.decode())
    name = name.decode()
    names.append(name)
    #sending no of questions
    client.sendall(str(TOT_NO_OF_QUESTIONS).encode())
    while(not started_quiz):
        pass
    print("Starting Sending Questions to " + name)
    while(ques_no < TOT_NO_OF_QUESTIONS):
        while(ques_no >= no_of_questions_entered):
            pass
        while(ques_no < no_of_questions_entered):
            #print("Sending Question")
            client.send((questions[ques_no]).encode())
            ans = client.recv(1024)
            #print(ans.decode())
            #answers.append((t1 - t0, player_no, t1 - t0, question_no, ans))
            print()
            if(ans.decode() == answers[ques_no]):
                anstot += 1
            print(name + " " + questions[ques_no] + " " + ans.decode())
            ques_no += 1
    print(name + " Answers " + str(anstot))
    client.close()


print("Quiz Program started")


print("Enter no of questions to be entered in quiz")
TOT_NO_OF_QUESTIONS = int(input())

s.bind((HOST, PORT))
s.listen(MAX_NO_OF_PLAYERS)

while True:
    print("Waiting for players to join ...")
    conn, addr = s.accept()
    t = Thread(target = client_conn, args=(conn, addr, no_of_players+1))
    t.start()
    no_of_players += 1
    print(str(no_of_players) + " players have joined")
    print("Press Y(Yes) to wait for more players or N(No) to start the Quiz")
    choice = input()
    if(choice == "N"):
        break

started_quiz = True

no_of_questions_entered = 0
while(no_of_questions_entered < TOT_NO_OF_QUESTIONS):
    print("Enter Question no. " + str(no_of_questions_entered+1))
    question = input()
    print("Enter Answer")
    answer = input()
    questions.append(question)
    answers.append(answer)
    no_of_questions_entered += 1

print("This is the end")
ended_quiz = True
