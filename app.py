import turtle
import time
delay = 0.1
game = True

#Initialise Window with the correct height, bg colour and tracer set to "0" tracer at zero ensures that the background won't constantly update.
win = turtle.Screen()
win.title("Snake in Turtle")
win.bgcolor("Black")
win.setup(width = 500, height=500)
win.tracer(0)

# block any possibility of turning back on itself
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# mark game as false when q is pressed to end game
def exit():
    global game
    game = False



#Initialise the turtle head object using the turtle class. assign a colour a shape, set its starting position and ensure penup is declared. "Pen Up" literally means the "pen"/pointer is not "down" and "drawing"
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#define move function to draw location of the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


#listen for keyboard press
win.listen()
win.onkey(exit, "q")
win.onkey(exit, "Escape")
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")

#declare main loop to keep updating the window and perform other functions
while game == True:
    win.update()
    move()
    time.sleep(delay)






