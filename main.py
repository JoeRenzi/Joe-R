import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.penup()



t2 = turtle.Turtle()
# t2.hideturtle()
t2.penup()

t.goto(0,0)
t.pendown()



t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

t.write("Joe's Favorites",font=("Arial",40,"bold italic"),align="center")
screen.bgcolor("lightblue")
enter = input("Press enter to continue: ")
t.clear()



t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor('purple')
t.begin_fill()
t.goto(25,50)
t.goto(0,100)
t.goto(-25,50)
t.end_fill()
t.penup()
t.goto(0,-70)
t.pendown()
t.penup()
t.write("page 1 - movie and sport",font=("Arial",32,"bold italic"),align="center")
t.penup()
t.goto(0,70)
t.pendown()
t.write("Basketball",font=("Arial",20,"bold italic"),align="center")
t.penup()
t.goto(0,-100)
t.pendown()
t.write("Goodfellas",font=("Arial",20,"bold italic"),align="center")
t.penup()
t.hideturtle()
screen.bgcolor('red')
t2.goto(0,250)
a = t2.stamp()
turtle.addshape("ball.gif")
t2.shape("ball.gif")



a = t2.stamp()

t2.goto(0,-250)
turtle.addshape("movie.gif")
t2.shape("movie.gif")
b = t2.stamp()

enter = input("Press enter to continue: ")
t.clear()
t2.clear()
t2.clearstamps()







screen.bgcolor("yellow")
t.penup()
t.goto(0,200)
t.write("page 2 - foods",font=("Arial",32,"bold italic"),align="center")
t.penup()
t.goto(-50,100)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.goto(50,100)
t.goto(0,200)
t.goto(-50,100)
t.end_fill()




t2.goto(50,-80)
turtle.addshape("chicken.gif")
t2.shape("chicken.gif")

a = t2.stamp()


t2.goto(-200,100)
turtle.addshape("mac.gif")
t2.shape("mac.gif")
b = t2.stamp()


t2.goto(-200,-50)
turtle.addshape("spag.gif")
t2.shape("spag.gif")
b = t2.stamp()



enter = input("Press enter to continue: ")


t.clear()
t2.clear()
t2.clearstamps()

screen.bgcolor("white")
t.goto(0,0)
t.write("page 3 - Hobbies",font=("Arial",32,"bold italic"),align="center")
t.fillcolor('blue')
t.begin_fill()
t.penup()
t.goto(0,150)
t.pendown()
t.circle(50)
t.end_fill()



t2.goto(130,130)
turtle.addshape("gym.gif")
t2.shape("gym.gif")

a = t2.stamp()


t2.goto(-100,-150)
turtle.addshape("game.gif")
t2.shape("game.gif")
b = t2.stamp()


t2.goto(100,-150)
turtle.addshape("ski.gif")
t2.shape("ski.gif")
b = t2.stamp()



t2.goto(-150,130)
turtle.addshape("espn.gif")
t2.shape("espn.gif")
b = t2.stamp()










turtle.done()


