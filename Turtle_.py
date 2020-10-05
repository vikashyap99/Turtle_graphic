import turtle 

kashyap = turtle.Turtle()
kashyap.speed(0)
kashyap.pencolor("blue")

for i in range(60):
    kashyap.forward(75)
    kashyap.left(123) 
    
kashyap.pencolor("red")
for i in range(100):
    kashyap.forward(120)
    kashyap.left(123)

kashyap.pencolor("green")
for i in range(200):
    kashyap.forward(350)
    kashyap.left(124)
    
turtle.done()

