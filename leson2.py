from turtle import *
#we want to paint a hause



#step 1: draw a square


width(7)
color("purple")


goto(0, -100)
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 100)
pendown()

#roof
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#window

penup()

goto(50, 20)
begin_fill()
pendown()
color("blue")
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()


#window 2
penup()

goto(180, 20)
begin_fill()
pendown()
color("blue")

forward(30)
right(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()



exitonclick()