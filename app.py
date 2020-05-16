import turtle
import time
import random
delay = 0.1
game = True
gamewidth = 500
gameheight = 500
score = 0
snake = []

#Initialise Window with the correct height, bg colour and tracer set to "0" tracer at zero ensures that the background won't constantly update.
win = turtle.Screen()
win.title("Snake in Turtle")
win.bgcolor("Black")
win.setup(width = gamewidth, height = gameheight)
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
#head.write("sometext")

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

#add text
scoretext = turtle.Turtle()
#score.speed(0)
#score.shape("square")
scoretext.color("red")
scoretext.penup()
scoretext.goto(-(gameheight / 2)+10,-(gameheight / 2)+10)
scoretext.write("Score: "+ str(score))
scoretext.hideturtle()

#add food at 40,40
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("yellow")
fruit.penup()
fruit.goto(random.randint(-(gamewidth / 2),(gamewidth / 2)), random.randint(-(gameheight / 2), (gameheight / 2)))

fruit.shapesize(1,1)

def reset_body():
    global score, snake
    time.sleep(2)
    head.goto(0, 0)
    head.direction = "stop"
    score = 0
    # segments of snake moved way off screen and then cleared.
    ## potential bug as the clear() function does not seem to clear all the drawings.
    for s in snake:
        s.goto(10000, 10000)
        # s.reset()
        s.clear()
    snake = []
    x, y = random.randint(-(gamewidth / 2) + 10,
                          (gamewidth / 2) - 10), random.randint(
        -(gameheight / 2) + 10, (gameheight / 2) - 10)
    fruit.goto(x, y)


#declare main loop to keep updating the window and perform other functions
while game == True:
    win.update()
    time.sleep(delay)
    # eat food
    if head.distance(fruit) < 20:
        x, y = random.randint(-(gamewidth / 2)+10,(gamewidth / 2)-10), random.randint(-(gameheight / 2)+10, (gameheight / 2)-10)
        fruit.goto(x, y)
        score += 20
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("orange")
        body.penup()
        snake.append(body)
    scoretext.clear()
    scoretext.write("Score: " + str(score))
    #step through snake list and move the end piece up through the list of locations.
    for i in range(len(snake)-1, 0, -1):
        x, y = snake[i-1].xcor(), snake[i-1].ycor()
        snake[i].goto(x, y)
    #for the front snake segment, move this to the position of the head.
    if len(snake) > 0:
        x,y = head.xcor(), head.ycor()
        snake[0].goto(x, y)

    # the board does not loop. the edges are collisions
    if head.xcor() < -(gamewidth / 2)+10 or head.xcor() > (gamewidth / 2)+10 or head.ycor() < -(gameheight / 2)+10 or head.ycor() > (gameheight / 2)+10:
        reset_body()


    #check for collisions with the snake head and the snake body
    move()
    for s in snake:
        if s.distance(head) < 1:
            reset_body()

    if head.direction != "stop":
        score +=1

    if score > 0:

        level = (score//100)
        print(level)
        extradelay = 0.01 * level
        print(extradelay)
        delay = 0.1 - extradelay






