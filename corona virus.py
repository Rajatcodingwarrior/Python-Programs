import matplotlib.pyplot as plt
import numpy as np
a=["JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUT","SEP"]
b=[11031,82189,998511,1260534,2112111,13550933,11780213,33754413,34286031]
plt.xlabel("Month name",fontsize=20)
plt.ylabel("Number of covid positive cases",fontsize=15)
plt.title("Bar graph of world showing covid-19 cases",fontsize=20)
plt.bar(a,b,color="blue",width=0.5)
plt.legend(["no of cases"])
plt.show()
