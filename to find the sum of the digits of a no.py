n=int(input("input any no="))
b=0
while n>0:
    c=n%10
    b=b+c
    n=n//10
print("sum of digits=",b)
