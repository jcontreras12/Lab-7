# Jose Contreras
# Date 11/13/21
# problem 3, write a Python function to multiply all the numbers in a list
n = (5, 2, 7, -1) # <= n is a set.  list=> n = [5, 2, 7, -1]
def multi(n):
    x = 1
    for i in n:
        x = x * i
        #print(x) it should be outside of the for loop
    print(x)
multi(n)   #need to call multi function with passing a set n 
 
