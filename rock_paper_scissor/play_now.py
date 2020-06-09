import random

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
elif(user_choice==1 and computer_choice==3):
    print("user chose ROCK, computer chose PAPER")
    print("computer wins!") 
elif(user_choice==2 and computer_choice==1):
    print("user chose SCISSOR, computer chose ROCK")
    print("computer wins!") 
elif(user_choice==2 and computer_choice==3):
    print("user chose SCISSOR, computer chose PAPER")
    print("user wins!") 
elif(user_choice==3 and computer_choice==1):
    print("user chose PAPER, computer chose ROCK")
    print("user wins!") 
elif(user_choice==3 and computer_choice==2):
    print("user chose PAPER, computer chose SCISSOR")
    print("computer wins!") 
