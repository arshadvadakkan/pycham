'''Define   a   function   that   accepts   2   values   and   return   its
 sum,   subtraction   and multiplication'''

# def addition(num1,num2):
#     return num1+num2
# def substraction(num1,num2):
#     return num1-num2
# def multiplication(num1,num2):
#     return num1*num2
# print("enter two number")
# num1=int(input())
# num2=int(input())
# add=addition(num1,num2)
# sub=substraction(num1,num2)
# mult=multiplication(num1,num2)
#
# print("addition is ",add)
# print("subtraction is ",sub)
# print("multiplication is " ,mult)

'''Define a function which counts vowels and consonant in a word: to =to+ i.count ("to")'''


def word(string):
    vowel = 0
    consonant = 0
    string=string.lower();
    for i in string:
        vowel = vowel + i.count("a","e","i","o","u")
    else:
         consonant = consonant + i.count()
string=input("enter word")
print(vowel)
print(consonant)