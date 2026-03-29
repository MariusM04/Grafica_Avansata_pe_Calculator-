import turtle
t = turtle.Turtle()
turtle.bgcolor("white")
t.pensize(3)
t.speed(10)

while True:
    for i in range(8):
        for colors in ["red", "blue", "magenta", "green", "olive", "turquoise", "violet", "indigo"]:
            t.color(colors)
            for _ in range(4):
                t.forward(100)  
                t.left(90)
            t.left(10)
    t.hideturtle()
    turtle.mainloop()