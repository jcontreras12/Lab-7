# Jose Contreras
# Date 11/13/21
# problem 4 write a python function that takes a list of numbers and returns a new list with unique elements of the list

def list(list):
        l = []
        for i in list:
            if i not in l:
                l.append(i)
        return l
 x = (1, 3, 3, 3, 6, 2, 3, 5)  #indentation error
x = [1, 3, 3, 3, 6, 2, 3, 5]
print(list(x))
