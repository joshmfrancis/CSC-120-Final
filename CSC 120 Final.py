# Joshua Francis
# December 9th, 2021
# CSC 120


#1.	Define a function that accepts student name and two scores (numbers), and computes the average of the two scores (numbers). It should output the student name and the average score. Sample output is shown in bold below. (The input is not in bold.)

#Enter you name: John 
#Enter two scores (numbers) with a space in between: 80 90

#John, you scored an average of 85

#(Grading of 30 points: Input of name – 5 points, Input of two numbers in one line – 5 points, Computing average – 5 points, Output of name and average – 5 points, Show output in exact format to professor in class – 10 points)

Name = input("Enter your Name:")

x, y = input("Enter two scores (numbers) with a space in between:").split()

n = (int(x) + int(y))/2

print(Name + ", you scored an average of", n)

# 2. Display the following pattern using nested FOR loops. (Grading of 40 points: show output to professor in class – 40 points)

stars = "* "                      # Defines stars for the function
def funct():                      # Names The function
    for x in range (1, 7, 1):     # Number of rows
        for y in range(1, 2, 1):  # How to count for the rows
            print(x*stars)        # Tells the function what to print
funct()                           # Calls the function

#3.	Using the turtle library, draw the following. (Grading of 30 points: Trapezoid-like face – 10 points, Circle-like eyes – 10 points, Show output to professor in class – 10 points, Solid fill color in eyes – BONUS 5 points,)

import turtle

t = turtle.Turtle()

t.shape("turtle")

t.color("blue") 
t.pensize(3) 
t.hideturtle()

t.forward(150)
t.left(-110)
t.forward(175)
t.left(-70)
t.forward(50)
t.left(-76)
t.forward(170)

t.penup()

t.goto(50, -50) # moves the turtle head to the eyes starting location

t.pendown() # moves the turtle pen down so it it ready to begin drawing the eyes

t.fillcolor("black")

t.begin_fill()

t.circle(15)

t.end_fill()

t.penup()

t.goto(100, -50)

t.pendown()

t.fillcolor("black")

t.begin_fill()

t.circle(15)

t.end_fill()

turtle.done()