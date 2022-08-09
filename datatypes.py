# a={"apple","banana"}
# print(a)
# print(len(a))
# print(type(a))
a=[]
b=[]
for i in range(1,101):
    if i%12==0:
      a.append(i)
      if i%14==0:
          b.append(i)
print(a)
print(b)