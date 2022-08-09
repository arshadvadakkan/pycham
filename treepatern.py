for r  in range(6):
    for c in range(7):
        if(r+c==3)or(r-c==-3) or(r==3 and 0==c-c) or (c==3 and 0==r-r) or(r==2 and 0!=c%6 ):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()