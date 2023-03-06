m=[]
a1={1:'jan',2:'feb',3:'mar',4:'apr',5:'may'}
a2={1:'efwefd',2:'fdfgdg',3:'vdsfds',8:'vfdf'}
a3=list(a1.keys())
a4=list(a2.keys())
for i in a3:
    for j in a4:
        if i==j:
            m=m+[i]
print(m)
            
