n=int(input("enter the no of nos="))
a=int(input("enter the no="))
b=int(input("enter the no="))
if a>b:
    max=a
    max2=b
else:
    max=b
    max2=a
for i in range(1,n-1):
    c=int(input("enter the no="))
    if c>max:
        max2=max
        max=c
    elif max>c>max2:
        max2=c
print("maximum=",max,"2max=",max2)
