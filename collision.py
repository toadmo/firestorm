from tkinter import *
import random


root = Tk()
root.geometry('1000x1000')
canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

# Need multiple balls moving around, collisions with triangle, rectangle, circle

def drawTriangle(x1, y1, x2, y2, x3, y3, color, width):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
    canvas.create_line(x2, y2, x3, y3, fill=color, width=width)
    canvas.create_line(x3, y3, x1, y1, fill=color, width=width)

def drawRectangle(x1,y1,x2,y2, color, width):
    canvas.create_line(x1,y1,x1,y2, fill=color, width=width)
    canvas.create_line(x1,y1,x2,y1, fill=color, width=width)
    canvas.create_line(x1,y2,x2,y2, fill=color, width=width)
    canvas.create_line(x2,y1,x2,y2, fill=color, width=width)

ball1 = canvas.create_oval(0,0,32,32,fill="blue", tag='ball')
ball2 = canvas.create_oval(15,15,47,47,fill="blue", tag='ball')
ball3 = canvas.create_oval(30,30,62,62,fill="blue", tag='ball')

balls = [ball1, ball2, ball3]

shapes = [drawTriangle(400, 475, 200, 350, 400, 150, 'black', 5), drawRectangle(450, 450, 550, 550, 'green', 5), canvas.create_oval(100,100,200,200,fill='yellow',tag='circle')]

speed_x1 = random.randint(-10,10)
speed_y1 = random.randint(-3,3)

while True:

# Each ball needs own initial spped

    for x in balls:
        canvas.move(x, speed_x, speed_y)
    canvas.after(50)
    canvas.update()

# Prevent balls from leaving screen

# Need to fix them being linked.

    for y in balls:
        coords = canvas.coords(y)
        if coords[0] <= 0:
            speed_x = random.randint(0,10)
        if coords[1] <= 0:
            speed_y = random.randint(0,3)
        if coords[2] >= 1000:
            speed_x = random.randint(-10,0)
        if coords[3] >= 1000:
            speed_y = random.randint(-3,0)

# Collision Detection:

# Difficulty with circular and triangular hitboxes
	
    if len(canvas.find_overlapping(550,550,650,650)) > 2:
        print("collision")
    

