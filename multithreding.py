import threading
def print_cube(num):
    print("cube:{}".format(num*num*num))
def print_square(num):
    print("square:{}".format(num*num))
if __name__=="__main__":

    #creating thread
    t1=threading.Thread(target=print_square,args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    #starting threas1
    t1.start()
    #starting thread 2
    t2.start()

    #wait until thread 1 is completely exicute

    t1.join()
    t2.join()
    print("done")