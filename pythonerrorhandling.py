try:
    file=open("file1.txt","r")
    file.write("abcd efg hijk")
except IOError:
    print("can't find file read data")
else:
    print("file writen succefully")
