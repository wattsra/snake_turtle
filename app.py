import turtle


#Initialise Window with the correct height, bg colour and tracer set to "0" tracer at zero ensures that the background won't constantly update.
win = turtle.Screen()
win.title("Snake in Turtle")
win.bgcolor("Black")
win.setup(width = 500, height=500)
win.tracer(0)


#Initialise the turtle head object using the turtle class. assign a colour a shape, set its starting position and ensure penup is declared. "Pen Up" literally means the "pen"/pointer is not "down" and "drawing"
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#declare main loop to keep updating the window and perform other functions
while True:
    win.update()





