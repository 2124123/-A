import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

def heart(scale, color):
    t.color(color)
    t.begin_fill()
    for i in range(360):
        rad = math.radians(i)
        x = scale * 16 * math.sin(rad) ** 3
        y = scale * (
            13 * math.cos(rad)
            - 5 * math.cos(2 * rad)
            - 2 * math.cos(3 * rad)
            - math.cos(4 * rad)
        )
        t.goto(x, y)  # ← corrigido: dentro do loop
    t.end_fill()

# Camadas escuras de fundo (sombra/profundidade)
for s in range(18, 13, -1):
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.width(2)
    heart(s, "#330000")

# Coração principal rosa
t.penup()
t.goto(0, -10)
t.pendown()
t.width(2)
heart(14, "#ffa1a1")

# Texto
t.penup()
t.goto(0, -170)
t.color("#B71130")
t.write(
    "I miss you ❤️",
    align="center",
    font=("Segoe UI", 22, "bold")
)

turtle.done()