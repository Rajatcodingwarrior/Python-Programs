lst=eval(input("enter list :"))
length=len(lst)
mean=sum=0
for i in range(0,length-1):
    sum+=lst[i]
mean=sum/length
print("given list is :",lst)
print("the mean of the given list is :",mean)
