def triangle(size:int)-> None:

    for i in range(1,size+1):
        for j in range(size-i):
            print("-",end="")
        for k in range(i,0,-1): #range(start,stop,step)
            if k%2 ==1:
                print('#', end="")
            else:
                print("*",end='')
        print()     #move to the next line
if __name__=="__main__":
    number=int(input("What's the size?"))
    triangle(number)    