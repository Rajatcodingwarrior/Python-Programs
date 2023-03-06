import pandas as pd
n=int(input("enter how many students are="))
r=[]
k=[]
for i in range(1,n+1):
    a=input("enter name of student=")
    a1=int(input(f"enter marks of{i} student of Maths="))   
    a2=int(input(f"enter marks of{i} student of Physics="))
    a3=int(input(f"enter marks of{i} student of Chemistry="))
    a4=int(input(f"enter marks of{i} student of English="))
    a5=int(input(f"enter marks of{i} student of IP="))
    s=[a1,a2,a3,a4,a5]
    r.append(s)
    k.append(a)
s=pd.DataFrame(r,index=k,columns=["Maths","Physics","Chemistry","English","IP"])
print("The result is here")
print(s)
