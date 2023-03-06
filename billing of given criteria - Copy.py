s=0
n=int(input("enter the no.of product"))
for i in range(1,n+1):
    m1=int(input("price of product"))
    q=int(input("enter quantity"))
    s=s+(m1*q)
if s>=1000:
    d=10
elif s>=2000:
    d=15
elif s>=5000:
    d=20
elif s>=10000:
    d=25
else:
    d=0
price=s-(s*0.01*d)
print("price to payed after discount is ",price,"and discount is ",d,"%")
