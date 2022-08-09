'''
1)write a program to coud the word "to""the"present in the text  file save the result in new file
2)write program to count upper case word
3)write a program to print odd and even position word into superate list
4) a write program to read 5 user name ,hobie,age into a hobie.txt file each user'''

# 1 ans)
# file=open("qua.txt","r")
# to=0
# the=0
# for i in file:
#     to =to+ i.count ("to")
#     the += i.count ("the")
#     # if "to" in i:
#     #     to=to+1
#     # if "the" in i:
#     # the=the+1
#
# print(to)
# print(the)
# file.close()
# file=open("result.txt","w")
# file.write(to,the)


# to=to+i.count("to")


# 2)ans

#
# def upper(string):
#     d={"upper":0}
#
#     for i in string:
#         if i.isupper():
#             d["upper"]+=1
#
#     print("string: ",string)
#     print("number of upper case charactor : " ,d["upper"])
# upper(input("enter the string"))


# ans3


#
# a=input("enter the string")
# odd=[]
# even=[]
# for i in range(len(a)):
#     if i%2==0:
#         odd.append(a[i])
#     else:
#         even.append(a[i])
# print("odd list : ",odd)
# print("even list : ",even)


# ANS4)

# for i in range(3):
#     name = input('Enter name : ')
#     hobie = input('Enter hobie : ')
#     age = input('Enter age : ')
#     print(name)
#     print(class_)
#     print(age)
#
import radius as radius

'''1)write a program to calculate area and circumference of circle rectangle square using class function
   2 write a program to create a class and using the class instant print all the attribute all object
   3 create a class teacher with name ,age, salary where salary must be privet can't be access 
   4) write a program that check if one class is subclass of another
   5) write a program to read a string and separate the odd even position word 
   6 write a program multi table 1 to 5
   7) make a list by taking 10 input from the user now delete all repeat element in list
   8 take a list all 10 element split it into middle and store element in two different list
   9)multiple two metrix
   10 write program spiral form'''

# area 2py r
# cic (py r)squar

# ans5) write a program to read a string and suparate the odd even position word
# a=input("enter the string")
# odd=[]
# even=[]
# for i in range(len(a)):
#     if i%2==0:
#         odd.append(a[i])
#     else:
#         even.append(a[i])
# print("odd list : ",odd)
# print("even list : ",even)

# ans6)
# num=int(input("enetr the number"))
# num=5
# for i in range(1,6):
#     print(num,'x',i,'=',num*i)


# ans9) multiple two metrix

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# b = [[9, 8, 7, ],
#      [6, 5, 4, ],
#      [3, 2, 1, ]]
#
# result = [[0, 0, 0, ],
#         [0, 0, 0, ],
#         [0, 0, 0, ]]
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             result[i][j] += a[i][k] * b[k][j]
# for r in result:
#     print(r)


# ans7) make a list by taking 10 input from the user now delete all repeat element in list

# animal = ["dog", "cat", "dog", "elephant", "cat", "monkey"]
# d = [*set(animal)]
#
# print(animal)
#
# print("repeated word deleted list :", d)

#ans4) write a program that check if one class is subclass of another

class mom:
    def m1(self):
        print("iam mother")
class son(mom):
    def s1(self):
        print("iam son")
i=son()
i.m1()
i.s1()

# ans10) write program spiral form
#
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# class

# write  a program to calculate area and circumference of circle rectangle square using class function
# length = int(input("enter the length and width of rectangle"))
# width = int(input())
# radius = float(input("enter the radius of circle"))
# side=int(input("enter the side of squar"))
# pi = 3.141592653589793238462643
# area = length * width
# circumference = 2 * (length + width)
# circlearea = pi * radius * radius
# circumferenceCircle = 2 * pi * radius
# areasquare=side*side
# circumferencesquare=4*side
# print("area of rectangle= ", area)
# print("circumference of rectangle=", circumference)
# print("area of circle=",circlearea)
# print("circumference of circle=",circumferenceCircle)
# print("area of square=",areasquare)
# print("circumference of square= ",circumferencesquare)
