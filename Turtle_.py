import turtle 

kashyap = turtle.Turtle()
kashyap.speed(0)
kashyap.pencolor("blue")

for i in range(60):
    kashyap.forward(50)
    kashyap.left(123) 
    
kashyap.pencolor("red")
for i in range(100):
    kashyap.forward(130)
    kashyap.left(123)

kashyap.pencolor("green")
for i in range(200):
    kashyap.forward(200)
    kashyap.left(123)
    
turtle.done()

