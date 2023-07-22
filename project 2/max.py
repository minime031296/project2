import turtle
colors=["red","purple","blue","green","orange","yellow","pink"]
t= turtle.Turtle()
t.begin_fill
turtle.bgcolor("white")
for x in range(50):
    t.pencolor(colors[x%7])
    t.fd(x*20)   
    t.right(90.1) 
    t.fd(x+50)
    t.rt(10)
    t.lt(190)
    t.fillcolor("yellow")
    t.fd(x*10)
    t.rt(160)
    t.color("yellow")
t.end_fill()
