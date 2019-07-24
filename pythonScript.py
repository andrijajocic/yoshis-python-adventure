import sys

#Sets input boxes for the integers

x=int(input("Type a number."))
y=int(input("Type a number."))

#Adds up inputed integers and prints out result

if x>y:
    print("X =" ,x ,"which is bigger than Y =",y)
elif x<y:
    print("X =" ,x ,"which is smaller than Y =",y)
elif x==y:
    print("X =" ,x ,"which is the same value as Y =",y)