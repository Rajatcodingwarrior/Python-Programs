#perfect no: sum of factors is equal than the no then it perfect no
n=int(input("input a no"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if n==s:
    print("it is a perfect no","sum of facors=",s)
else:
    print("it is not a perfect no","sum of facors=",s)
