n=int(input("input any no="))                  #armstrong no is a no where the sum of the cube of its digits is equal to the orignal no 
m=n
c=0
while n>0:
    b=n%10
    c=c+b**3
    n=n//10
if c==m:
    print("it is a armstrong no",c,"=",m)
else:
    print("it is not a armstrong no")
