import turtle as tu

roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Hilbert Curve")
roo.left(90)
roo.speed(0)
roo.penup()
roo.goto(-100, -100)  
roo.pendown()

def draw(l):
    if l < 10: 
        return
    else:
        roo.pensize(1)
        roo.pencolor("cyan")
        roo.forward(l)
        roo.left(90)  # unghiul a fost modificat
        draw(l * 0.5)  # lungime diferita
        roo.right(180)  # unghiul complementar celui din stanga
        draw(l * 0.5)
        roo.left(90)
        roo.backward(l)

#automatizarea recursivitatii
for _ in range(4):
    draw(150) 
    roo.right(90)  # formele apar la 90 de grade una fata de cealalta

wn.exitonclick()