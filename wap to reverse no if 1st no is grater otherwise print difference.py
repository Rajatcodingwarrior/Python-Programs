#wap to input 2 nos if the first no is larger then change their value and print them otherwise print the positive difference between nos
a=int(input("enter a  1st no="))
b=int(input("enter a  2st no="))
if a>b:
    c=a
    a=b
    b=c
    print("reversed nos=",a,b)
else:
    print("difference=",b-a)
    
