import turtle

# Configuração da tela
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("BMW Drawing Animation")

t = turtle.Turtle()
t.speed(1)
t.pensize(2)

# Função para desenhar círculo
def draw_circle(radius, color, fill=False):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.color(color)
    t.pendown()

    if fill:
        t.begin_fill()

    t.circle(radius)

    if fill:
        t.end_fill()

# Função para desenhar quadrantes
def draw_quadrant(radius, start_angle, color):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.color(color)
    t.begin_fill()
    t.pendown()

    t.forward(radius)
    t.left(90)
    t.circle(radius, 90)
    t.goto(0, 0)

    t.end_fill()

# Função para escrever BMW
def write_text():
    t.penup()
    t.color("white")
    radius = 120
    font_size = 22

    letters = [("B", 150), ("M", 90), ("W", 30)]

    for letter, angle in letters:
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.setheading(angle - 90)
        t.write(letter, align="center", font=("Arial", font_size, "bold"))

# Desenho do logo
draw_circle(145, "white")
draw_circle(140, "white")
draw_circle(135, "black", fill=True)

radius_inner = 95

draw_quadrant(radius_inner, 0, "white")
draw_quadrant(radius_inner, 90, "#0066AD")
draw_quadrant(radius_inner, 180, "white")
draw_quadrant(radius_inner, 270, "#0066AD")

draw_circle(radius_inner, "white")

write_text()

t.hideturtle()
turtle.done()