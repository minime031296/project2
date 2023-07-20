import turtle
colors=["red","purple","blue","green","orange","yellow"]
t= turtle.Turtle()
turtle.bgcolor("cyan")
for x in range(50):
    t.pencolor(colors[x%6])
    t.fd(x*20)   
    t.right(90.1) 
    t.lt(90)
    t.rt(90.1)
    t.color("yellow")
    t.begin_fill()
    
    t.end_fill()

