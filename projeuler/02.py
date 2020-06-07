#def fib(n):
#   a = 0
#    b = 1

#    print(a)
    #print(b)

a = 1
b = 1
c = 1
mysum = 0
while (c <= 4000000):    
    c = a + b
    a = b
    b = c
 

    if (c % 2 == 0):
        mysum = c + mysum 
        print(mysum)

    
