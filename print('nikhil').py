#day4

# print("hello world",5)
# print(5)
# print(7*9)
# print(5+6)

# #day5: comments, escape squence

# # "#" ise comment kehte hai
# # \n line change kr k print krta hai or ise escape squence kehte hai
# print("hey nikhil \nhow are you")

# # \" ise use krne se highlight ho jata hai
# print("hey i am a \"good boy\" \nand this viewer is also a good boy")

# print("hey",6,7, sep="~", end="009\n")
# print("nikhil")

# # day 6 variables and data types
# # int= numbers, float= decimal numbers, string= name, boolian= true or false
# # list= collection of everything and it is mutable which means can be change
# # tuple= collection of everything but is not mutable i.e, cannot be change
# # dictionary = collection of data

# a=1
# print(a)
# b= "Nikhil"
# print(b)
# c= True
# print(c)
# print("the type of a is" , type(a))
# print("the type of b is" , type(b))
# print("the type of c is" , type(c))

# list1 = [8,2.3, -4,"apple"]
# print(list1)

# tuple1 = {"parrot", "sparrow", 2}
# print(tuple1)

# dict1 = {"name": "Sakshi", "age": 22, "canvote":'true'}
# print(dict1)

# day 7 operators

# d=5
# e=3
# print("the value of", d+e)
# print("the value of", d-e)
# print("the value of", d*e)
# print("the value of", d/e)
# print("the value of", d//e)
# print("the value of", d**e)

# day 10 user input

# f= input()
# print("my name is",f)

# g= input("enter your name:")
# print("my name is",g)

# x= input("first no: ")
# y= input("second no: ")
# print("sum of x and y is",int(x) + int(y))

# day11 strings

# name= "nikhil"
# print("hello"+name)

# apple= '''he said,
# hi nikhil
# "i want to eat an apple"
# good'''
# print(apple)

# a= 1,2,3,4,5
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

#for loop
# a= "nikhil"
# for char in a:
#     print(char)

#day12 string slicing

# fruit= "mango"
# mangolen = len(fruit)
# print(mangolen)
# print(fruit[0:5])
# print(fruit[1:3])
# print(fruit[0:-2])
# print(fruit[-5:-2])

#day13 string methods (strings are immutable)

# a= "!!!!Nikhil!!!!"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Nikhil", "John"))

# b= "nikhil johny sins"
# print(b.split(" "))

# c="introduction to python"
# print(c.capitalize())

# d= "welcome home"
# print(len(d))
# print(len(d.center(50)))
# print(d.count("o"))

# a="channa mereya"
# print(a.startsswith("channa"))
# print(a.endswith("mereya"))
# print(a.endswith("m",0,8))

# str1= "he's is a good boy"
# print(str1.find("is"))

# a="gtavicecity01"
# print(a.isalpha())
# print(a.isalnum())
# print(a.islower())
# print(a.isupper())
# print(a.isprintable())
# print(a.isspace())
# print(a.istitle())
# print(a.swapcase())

#day 14 if else

# a= int(input("enter your age:"))
# print("your age is:",a)

# if(a>=18):
#     print("you can drive")

# else:
#     print("you cannot drive")    

# conditional operators: >,<.>=.<=

# a= int(input("enter the number:"))

# if(a>0):
#     print("the number is positive")

# elif(a==0):
#     print("the number is zero")  

# else:
#     print("the number is negative")

# num = int(input("enter the number"))
# if(num < 0):
#     print("the number is negative")

# elif(num > 0):
#     print("the number is between 1-10")
#     if(num >10 and num <= 20):
#         print("number is between 11-20")

#     else:
#         print("the number is greater than 20")     

# else:
#     print("the number is zero")       

#day 16 match case

# x= int(input("enter the value of x:"))

# match x:

#     case 0:
#         print("x is zero")

#     case 2:
#         print("x is two")

#     case _ if x!=90:
#         print("x is not 90")

#     case _ if x!=80:
#         print("x is not 80")

#     case _:
#         print(x)                

# day 17 for loops

# name= "Nikhil"
# for i in name:
#     print(i)
            
# colors= ["Red", "Green", "Blue"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(10):
#     print(k)

# for k in range(1,10):
#     print(k)

# for k in range(10):
#     print(k+1)

# for k in range(1,12,3):
#     print(k)

# day 11 while loops

i=0
while(i<3):
    print(i)
    i=i+1








