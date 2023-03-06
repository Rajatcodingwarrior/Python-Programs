a=0
b=1
n=int(input("enter a no"))
print(a,end="  ")
for i in range(n-1):
    a=b
    b=a+b
    print(a,end="  ")
