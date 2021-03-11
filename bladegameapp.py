import random
import turtle
import time
delay = 0.15

pencere = turtle.Screen()
pencere.title('Blade Snake Game')
pencere.bgcolor('white')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("circle")
kafa.color("red")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("black")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("circle")
yaz.color("darkred")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Score: {}".format(puan), align="center", font=("Italic", 24, "normal"))
yaz.penup()
yaz.hideturtle()
yaz.goto(0, -260)
yaz.write("The game will speed up after the first game!", align="center", font=("Italic", 12, "normal"))

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"
def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"





def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"
def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

        puan = 0
        delay = 0.1

        yaz.clear()
        yaz.write("Score: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("grey")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Score: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Score: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15

    time.sleep(delay)