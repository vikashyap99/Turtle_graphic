
import turtle 

# function defining the moves to print each character of the name
def fun(c,k):
    
    if c=='A' or c=='B'  or c=='E' or c=='F':
        k.forward(30)
        k.right(90)
        k.forward(25)
        k.backward(25)
        k.left(90)
        k.forward(30)
        k.right(90)
        k.forward(25)
        k.right(90)
        if c=='E' or c == 'F':
            k.penup()
            
        k.forward(60)
        k.pendown()


        if c == 'B' or c=='E':
            k.right(90)
            k.forward(25)
            k.backward(25)
            k.left(90)

    elif c=='C' or c=='D' or c=="O" or c=="U":
        k.forward(60)
        k.right(90)
        if c=='U':
            k.penup()

        k.forward(30)
        k.pendown()
        if c == 'C':
            k.penup()
    
        k.right(90)
        k.forward(60)
        k.pendown()
        k.right(90)
        k.forward(30)
        k.backward(30)
        k.left(90)

    elif c == 'G':
        k.forward(60)
        k.right(90)
        k.forward(30)
        k.penup()
        k.right(90)
        k.forward(30)
        k.pendown()
        k.right(90)
        k.forward(15)
        k.backward(15)
        k.left(90)
        k.forward(30)
        k.right(90)
        k.forward(30)
        k.backward(30)
        k.left(90)
    elif c == 'H':
        k.forward(60)
        k.backward(30)
        k.right(90)
        k.forward(25)
        k.left(90)
        k.forward(30)
        k.backward(60)
        k.right(180)
    elif c == 'I' or c=='J':
        k.penup()
        k.forward(60)
        k.pendown()
        k.right(90)
        k.forward(30)
        k.backward(15)
        k.right(90)
        k.forward(60)
        k.right(90)
        k.forward(15)
        if c=='J':
            k.right(90)
            k.forward(20)
            k.backward(20)
            k.left(90)
            k.penup()
        k.backward(30)
        k.left(90)
        k.pendown()
    elif c == 'K':
        k.forward(60)
        k.backward(30)
        k.right(45)
        k.forward(40)
        k.backward(40)
        k.right(90)
        k.forward(45)
        k.right(45)
    elif c=='L':
        k.forward(60)
        k.backward(60)
        k.right(90)
        k.forward(25)
        k.right(90)
    elif c == "M":
        k.forward(60)
        k.right(135)
        k.forward(30)
        k.left(90)
        k.forward(30)
        k.right(135)
        k.forward(60)
    elif c == "N":
        k.forward(60)
        k.right(150)
        k.forward(70)
        k.left(150)
        k.forward(60)
        k.backward(60)
        k.right(180)
    elif c == "P"  or c=="R":
        k.forward(60)
        k.right(90)
        k.forward(30)
        k.right(90)
        k.forward(30)
        k.right(90)
        k.forward(30)
        if c=="P":
            k.penup()
        k.left(135)
        k.forward(40)
        k.pendown()
        k.right(45)

    elif c == "Q":
        k.forward(60)
        k.right(90)
        k.forward(30)
        k.right(90)
        k.forward(60)
        k.right(90)
        k.forward(30)
        k.right(135)
        k.penup()
        k.forward(30)
        k.right(90)
        k.pendown()
        k.forward(35)
        k.right(45)
    elif c == "S":
        k.right(90)
        k.forward(30)
        k.left(90)
        k.forward(30)
        k.left(90)
        k.forward(30)
        k.right(90)
        k.forward(30)
        k.right(90)
        k.forward(30)
        k.right(90)
        k.penup()
        k.forward(60)
    elif c == "T":
        k.penup()
        k.forward(60)
        k.pendown()
        k.right(90)
        k.forward(30)
        k.backward(15)
        k.right(90)
        k.forward(60)
        k.left(90)
        k.penup()
        k.forward(15)
        k.right(90)
    elif c=="V" or c=="W":
        if c=="V":
            i=1
        else :
            i=2
        for j in range(i):
            k.penup()
            k.forward(60)
            k.right(170)
            k.pendown()
            k.forward(60)
            k.left(160)
            k.forward(60)
            k.right(170)
            k.penup()
            k.forward(60)
            k.left(180)
        
        k.right(180)
    elif c=="X" or c=="Y":

        k.right(30)
        k.forward(65)
        k.left(120)
        k.penup()
        k.forward(30)
        k.pendown()
        k.left(120)
        k.forward(32.5)
        if c == "Y":
            k.penup()
        k.forward(32.5)
        k.right(30)
        k.pendown()
    
    elif c == " ":
        k.right(90)
        k.penup()
        k.forward(10)
        k.right(90)
        k.pendown()

    else :
        k.right(30)
        k.forward(65)
        k.left(120)
        k.forward(30)
        k.left(90)
        k.penup()
        k.forward(57)
        k.pendown()
        k.left(90)
        k.forward(30)
        k.right(90)

    
        

    k.up()
    k.left(90)
    k.forward(15)
    k.left(90)
    k.down()
    #k.done()
    
    

x = input("Enter your name : " )
x = x.upper()
k = turtle.Turtle()
k.speed(0)
k.pencolor("blue")
k.pensize(6)
k.left(210)
k.penup()
k.forward(300)
k.pendown()
k.right(90)

for i in x:
    fun(i,k)

kashyap = turtle.Turtle()
kashyap.speed(0)
kashyap.pencolor("blue")
kashyap.penup()
kashyap.left(180)
kashyap.forward(200)
kashyap.right(90)
kashyap.forward(200)
kashyap.pendown()

for i in range(60):
    kashyap.forward(75)
    kashyap.left(123) 
    
kashyap.pencolor("red")
for i in range(100):
    kashyap.forward(120)
    kashyap.left(123)



a = turtle.Turtle()
a.speed(0)
a.pencolor("green")
a.penup()
a.forward(100)
a.right(90)
a.forward(50)
a.pendown()

for i in range(200):
    a.forward(350)
    a.left(124)
    
turtle.done()






