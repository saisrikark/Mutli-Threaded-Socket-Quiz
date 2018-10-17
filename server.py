from threading import Thread
import socket
import time

def new_client(client, addr):
    name = client.recv(1024)
    while(not started_quiz):
        pass
    #while(not ended_quiz):
        
    client.close()


s = socket.socket()
host = socket.gethostname()
print(host)
port = 5002

print("Quiz started")

s.bind((host, port))
s.listen(5)

no_of_players = 0
started_quiz = False
ended_quiz = False

while True:
    print("Waiting for players to join ...")
    c, addr = s.accept()
    t = Thread(target=new_client, args=(c, addr))
    no_of_players += 1
    print(str(no_of_players) + " players joined")
    print("Press Y(Yes) to wait for more players or N(No) to start the Quiz")
    choice = input()
    if(choice == "N"):
        break

started_quiz = True

print("Enter no of questions")
no_of_questions = int(input())
while(no_of_questions > 0):
    print("Enter a Question")
    question = input()
    
    no_of_question -= 1

ended_quiz = True