# Jose Contreras
# Date 11/13/21
# problem 2 write a python function to check weather a number is in a given range. range is 1-10
def Range(i):
    #if i in range(1-11): incorrect use of parameter.
     if i in range(1, 11):
        print(i, " number is in range")
    else:
        print(i, "number is not in range")
        
#Function Call Statement
num = int(input("enter a number to check if it is in range (1, 10):"))
Range(num)
        
