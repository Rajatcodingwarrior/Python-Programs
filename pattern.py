a=int(input("enter a no"))
if a%2==0:
    for i in range(0,a+1):
        for j in range(a,i,-1):
            print("*",end="")
        print()
else:
    for i in range(1,a+1):
        for j in range(1,i):
            print("#",end="")
        print()
