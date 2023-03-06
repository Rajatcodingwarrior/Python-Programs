s=0
a=int(input("enter a no"))
for i in range(1,a+1):
    if a%i==0:
        s+=1
if s==2:
    print("it is a prime no",a)
elif s==1:
    print("it is neither prime nor composite",a)
else:
    print("it is a composite no",a)
    
