import pandas as pd
a=["A","B","C","D","E"]
b=[12000,12500,11000,11000,11300]
g=pd.Series(b,a)
k=g.sort_values()
s=0
for i in range (5):
    s=s+k[i]
print("max=",k[4],"min=",k[0],"avg=",s/5)
