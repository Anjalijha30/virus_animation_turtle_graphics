import turtle

a,b=0,0
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
l=["red","yellow","green","blue","pink"]
while True:
    k=a%5
    turtle.pencolor(l[k])
    turtle.forward(a)
    turtle.right(b)
    a+=3
    b+=1
    if b==201:
        break
    
