# n=int(input("enter limit"))
# for i in range(0,n):
#
#     for j in range(0,i+1):
#
#         print("*" ,end=' ')
#     print("\n")
# n=int(input("enter limit"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print("\n")
# start=65
# # n=int(input("enter limit"))
# for i in range(65,n):
#     for j in range(65,i+1):
#
#         print(chr(start),end=" ")
#         start=start+1
#     print('\n')

n=int(input("enter limit"))

for i in range(1,n+1):
    start=65
    for j in range(1,i+1):

        print(chr(start),end=" ")
        start=start+1

    print('\n')