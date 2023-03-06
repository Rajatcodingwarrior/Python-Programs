import turtle
t=turtle.Turtle()
turtle.bgcolor("blue")
turtle.speed(0)
for i in range(10):
    for j in range(15):
        a,b=10,20
        for k in range(20):
            t.fillcolor("red")
            t.begin_fill()
            t.forward(b)
            t.left(a)
            t.forward(a)
            t.right(b)
            a=a+2
            b=b+30
            t.end_fill()
            

