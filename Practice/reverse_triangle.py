size=int(input("What's the size? "))

for i in range(1,size+1):
    for j in range(size-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(f"{k}",end="")
    print("")


# for i in range(1,size+1):
#     for k in range(i,1,-1):
#         print(" ",end="")

#     for j in range(size-i+2,1,-1):
#         print(f"{j-1}",end="")

#     print("")


# for i in range(1,size+1):
#     for k in range(i,1,-1):
#         print(" ",end="")

#     for j in range(1,size+2-i):
#         print(f"{j}",end="")

#     print("")

