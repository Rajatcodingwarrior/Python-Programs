n=int(input("input any no="))
c=0
while n>0:
    b=n%10
    c=c+1
    n=n//10
print("no of digits",c)
