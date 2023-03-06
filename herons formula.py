a=int(input("enter the first side of the triangle"))
b=int(input("enter the second side of the triangle"))
c=int(input("enter the third side of the triangle"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is ",area)
