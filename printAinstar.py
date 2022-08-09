for r  in range(4):
    for c in range(7):
        if(r+c==3)or(r-c==-3) or (r==2 and c==3):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
