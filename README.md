from turtle import*
color("black","red")
pensize(5)
title("马万骁")

begin_fill()
speed(3)
penup()
goto(x=50,y=50)

pendown()
right(45)
goto(100,0)
left(90)
forward(120)
circle(50,225)

penup()
goto(0,0)

pendown()
left(135)
forward(120)
circle(50,225)
seth(90)
circle(50,225)
forward(121)
end_fill()

left(56)
penup()
goto(-210,40)

pendown()
goto(0,80)
penup()
goto(160,110)
pendown()
goto(320,140)

done()
