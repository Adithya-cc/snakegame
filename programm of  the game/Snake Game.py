# Snake game

import os
import turtle
import time
import random

delay = 0.1

#score
score=0
high_score=0
wn = turtle.Screen()
wn.title("SnakeGame")
wn.bgcolor("black")
wn.bgpic("backgroung1.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#obj player
turtle.register_shape("body.gif")
turtle.register_shape("head.gif")
turtle.register_shape("food.gif")

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("head.gif")
head.color("blue")
head.penup()
head.goto(-100,-20)
head.direction = "stop"
head.setheading(90)

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("food.gif")
food.color("red")
food.penup()
food.goto(-100,100)

segments = []

#scorepe("square")
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "right", font = ("Courier", 18, "bold"))

# function
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_pass():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "stop":
        x = head.xcor()
        y = head.ycor()
        head.sety(y)
        head.setx(x)    
# Keyboard Cont
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_pass,"space")

#main game loop
while True:
    wn.update()

    #check touch border
    if head.xcor()>180 or head.xcor()<-380 or head.ycor()>240 or head.ycor()<-260:
        time.sleep(1)
        head.goto(-100,0)
        head.direction = "stop"

        
        x = random.randint(-380,180)
        y = random.randint(-260,240)
        food.goto(x,y)
        

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        #Reset score
        score = 0

        #reset the delay
        delay = 0.1
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "right", font = ("Courier", 18, "bold"))


    # eat food
    if head.distance(food) < 20:
        x = random.randint(-380,180)
        y = random.randint(-260,240)
        food.goto(x,y)
        
        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("body.gif")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay  
        delay -= 0.001

        #increas score
        score += 10
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "right", font = ("Courier", 18, "bold"))
                
    #Move the segment in the order
    for index in range(len(segments)-1, 0, -1):             
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()        
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        

    move()

    #boddy collution
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(-100,0)
            head.direction = "stop"

            
            x = random.randint(-380,180)
            y = random.randint(-260,240)
            food.goto(x,y)
            

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            #Reset score
            score = 0

            #reset the delay
            delay = 0.1

            # updat score
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align = "right", font = ("Courier", 18, "bold"))
   
    time.sleep(delay)
    
wn.mainloop()
