from turtle import *
speed(0)
setposition(-40, -30)
bgcolor("black")
color("aqua")
for i in range(160):
    rt(i)
    circle(170, i)
    fd(100)
    right(240)
    fd(i)
    lt(1)
    hideturtle()
done()