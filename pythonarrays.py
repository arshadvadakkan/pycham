# a=["cat","dog","fish"]
# print(a)
# print(a[0])


a=["cat","dog","fish"]
b=[" milk"," chicken","  pellets"]
s=[i+j for (i,j) in zip(a,b)]
print(s)