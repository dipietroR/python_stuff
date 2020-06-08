    
import random

myrand=random.randint(0,101)
#print(myrand) # for debug

while True:
    user = int(input("enter a number between 0,101: "))
    print(user)
    if(user==myrand):
        print("You are right!")
        break
    elif(user<myrand):
        print ("Too low! Try again.")
    elif(user>myrand):
        print("Too high! Try again.")

