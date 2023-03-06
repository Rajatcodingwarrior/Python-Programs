import matplotlib.pyplot as plt
import numpy as np
n=int(input("enter the no of student="))
a1=[]
b1=[]
for i in range(1,n+1):
      a=input(f"enter the name of {i} student:")
      b=int(input("enter marks of {i}student:"))
      a1.append(a)
      b1.append(b)
      
plt.xlabel("Name",fontsize=20)
plt.ylabel("Marks",fontsize=15)
plt.title("Examination analysis",fontsize=20)
plt.bar(a1,b1,color="m",width=0.8)
plt.legend(["marks"])
plt.show()
