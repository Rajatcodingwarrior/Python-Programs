n=int(input("input any no="))
b=0
while n>0:
    c=n%10
    n=n//10
    if c%2==0:
        b=b+c
print("sum of the even digits=",b)
    
