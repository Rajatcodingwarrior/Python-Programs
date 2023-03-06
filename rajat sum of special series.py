s=0.0                                           # series S=ax/2!+ax**3/4!+..........+nth term
a=int(input("enter the value of a="))
n=int(input("entyer no of times n="))
x=int(input("enter the value of x="))
for i in range(1,2*n-1,2):
    f=1
    for j in range(1,i+2):
        f=f*j
        s=s+a*x**i/f
print("sum=",s)
