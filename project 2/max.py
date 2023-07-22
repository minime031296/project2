import turtle
colors=["red","purple","blue","green","orange","yellow","pink"]
jeff= turtle.Turtle()
jeff.begin_fill
turtle.bgcolor("white")
for x in range(15):
    jeff.pencolor(colors[x%6])
    jeff.circle(100)
    jeff.fd(1)
    jeff.rt(1600)
    jeff.rt(100)

