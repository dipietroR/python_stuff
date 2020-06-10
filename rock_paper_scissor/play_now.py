import random

user_score = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    
    computer_choice=random.randint(1,3)
    #print(computer_choice) #debug 

    print ("1==Rock")
    print ("2==Scissor")
    print ("3==Paper")

    user_choice = int(input("enter a number between 1,3: "))

    if (user_choice==computer_choice):
        print("Tie!")
    elif(user_choice==1 and computer_choice==2):
        print("user chose ROCK, computer chose SCISSOR")
        print("user wins!") 
        user_score = user_score + 1
    elif(user_choice==1 and computer_choice==3):
        print("user chose ROCK, computer chose PAPER")
        print("computer wins!") 
        computer_score = computer_score + 1
    elif(user_choice==2 and computer_choice==1):
        print("user chose SCISSOR, computer chose ROCK")
        print("computer wins!") 
        computer_score = computer_score + 1
    elif(user_choice==2 and computer_choice==3):
        print("user chose SCISSOR, computer chose PAPER")
        print("user wins!") 
        user_score = user_score + 1
    elif(user_choice==3 and computer_choice==1):
        print("user chose PAPER, computer chose ROCK")
        print("user wins!") 
        user_score = user_score + 1
    elif(user_choice==3 and computer_choice==2):
        print("user chose PAPER, computer chose SCISSOR")
        print("computer wins!") 
        computer_score = computer_score + 1

    print("user: " + str(user_score) + " and computer: " + str(computer_score))


