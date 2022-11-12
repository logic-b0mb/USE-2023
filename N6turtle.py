from turtle import *
tracer(0)
r=50
for i in range(4):
    fd(12*r)
    rt(150)
    fd(12*r)
    rt(30)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*r,y*r)
        dot(3,'blue')
update()
exitonclick()
    
