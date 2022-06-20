import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Ghadi")
screen.tracer(0)

kalam = turtle.Turtle()
kalam.hideturtle()
kalam.speed(0)
kalam.pensize(3)

def ghadi_bana(ghantaa, minutee, secondd,kalam):

    kalam.up()
    kalam.goto(0,210)
    kalam.setheading(180)
    kalam.color("red")
    kalam.pendown()
    kalam.circle(210)

    kalam.up()
    kalam.goto(0,0)
    kalam.setheading(90)

    for z in range(12):
        kalam.fd(190)
        kalam.pendown()
        kalam.fd(20)
        kalam.penup()
        kalam.goto(0,0)
        kalam.rt(30)

    hands = [("black", 80, 12), ("black", 150, 60), ("black", 110, 60)]
    time_set = (ghantaa, minutee, secondd)

        for hand in hands:
            time_part = time_set[hands.index(hand)]
            angle = (time_part/hand[2])*360
            kalam.penup()
            kalam.goto(0,0)
            kalam.color(hand[0])
            kalam.setheading(90)
            kalam.rt(angle)
            kalam.pendown()
            kalam.fd(hand[1])

while True:
    ghantaa = int(time.strftime("%|"))
    minutee = int(time.strftime("%M"))
    secondd = int(time.strftime("%S"))

    ghadi_bana(ghantaa, minutee, secondd, kalam)
    screen.update()
    time.sleep(1)
    kalam.clear()
