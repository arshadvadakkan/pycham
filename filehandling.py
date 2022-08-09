# filename="file1.txt"
# file=open(filename,"r")
# # for line in file:
# #     print(line)
# print(file.read(19))
# print(file.readline())
# print(file.readlines())
# file.close()


#writing

# file=open("file1.txt","w")
# file.write("vadakkan house")
# file.close()
# file=open("file1.txt")
# print(file.read())
# file.close()
#
# file=open("file1.txt","a")
# file.write("abcd")
# file.close()
# file=open("file1.txt")
# print(file.read())

#creating a new file

# f=open("abc.txt","x")
# f.close()

#remove file
# import os
# os.remove("abc.txt")



# import os
# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
# else:
#     print("not exist")

# import  os
# os.rmdir("123.txt")


#get current directory
#import os
#os.getcwd()

#change directory

# import os
# #os.chdir("C:\Users\HP\Desktop\note")
# print("1",os.getcwd())
# print(os.listdir())

'''making new diractory'''
import os
os.makedirs("demodir")
print(os.listdir())

