s=0
n=int(input('enter a no'))
for i in range(1,n+1):
    if n%i==0:
        s=s+1
print("sum of factor=",s)
