from tkinter import Variable
from turtle import right
from unittest import result, skip


a = 20
b = 15.5
c = -5739
print(a,b,c) # type() to Cheak Type value 


num1 = 50 #integer
num2 = 10.5 #float
result = num1 + num2
print(result)

a= "a" #single Line String
print(a)

a=""" good morning
Teacher and every body  """ #multiline Strings
print(a)
print(len(a)) # Chack Long String

times = 3
hi = "Hello"

result = hi * times
print(result) # 

msg =  "MR. Patsakorn"
print(msg[0]) # [] Square Brackets

x= "HELLO WORLD"
print(x.lower()) #.lower(),.upper()

x= "I wanna learn python , I really like it"
y = x.split(",") # split() befult methods is (" ") you can change split methods in () example : split(",") 
print(y)

x= "i love python"
print(x.capitalize()) #uppercase only first character

animals = ["Cat","Dog", "Pig"] #append() add to list ,insert( {index}, "")
animals.append("Cow")
animals.insert(0 , "Rat")
print(animals)

colors = ("Red","Green","Blue") #tuple can not change data ?? = () 

print(colors)


# Dictionary Dict => Key&value

variable = {
    "key": "value",
    }

inp_name = input("Type your name here :") #input defult: string
inp_age = input("Type your age here :")

student = {
    "name" : inp_name,
    "age" : int(inp_age)
}

print(student["name"]) # ["key"]
print(student["age"]) # ["key"]