#wap tpo input any no if it is even print its double otherewise print its table
a=int(input("enter a no="))
if a%2==0:
    print("double=",2*a)
else:
    for i in range(1,11):
        print(a,"x",i,"=",a*i)
