# a=["adul","aman","arun"]
# b=["a123","b123","c123"]
# n=input("enter name")
# p=input("enter pwrd")
# if (a[0]==n and b[0]==p ) or (a[1]==n and b[1]==p) or (a[2]==n and b[2]==p):
#     print("login success")
# else:
#     print("login filed")
a=["adul","aman","arun"]
b=["a123","b123","c123"]
n=input("enter name")
if n in a:
    p=input("enter password")
    ind=a.index(n)
    if p in b and ind==b.index(p):
        print("welcome")
    else:
        print("incorrect password")
else:
    print("invalid name")