s=0
n=int(input("enter the no. of subjects"))
for i in range(1,n+1):
    m1=int(input("enter the marks of subject out of 100"))
    s=s+m1
per=s/n
if per>=90:
    grade="A+"
elif per>=80:
    grade="A-"
elif per>=70:
    grade="B"
elif per>=50:
    grade="C"
else:
    grade="f"
print("percentage is ",per,"and grade is ",grade)
