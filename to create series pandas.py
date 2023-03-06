a=[31,28,31,30,31,30,31,31,30,31,30,31]
b=["jan","feb","mar","april","may","june","july","aug","sept","oct","nov","dec"]
import pandas as pd
c=pd.Series(a,b)
print(c)
