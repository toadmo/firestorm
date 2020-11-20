from tkinter import *
import random

root = Tk()
root.geometry('500x500')
canvas = Canvas(root, height=500, width=500)
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

ball1 = canvas.create_oval(300,300,332,332,fill="blue", tag='ball')
ball2 = canvas.create_oval(350,350,382,382,fill="blue", tag='ball')
ball3 = canvas.create_oval(270,270,302,302,fill="blue", tag='ball')

balls = [ball1, ball2, ball3]

# Stored Coordinates
tri_coords = [400, 475, 200, 350, 400, 150]
circ_center = [160, 160]


shapes = [canvas.create_polygon(10,10, 10,100, 100,100, 100,10), 
canvas.create_polygon(tri_coords, outline='#f11', fill='red', width=2), 
canvas.create_oval(120,120,200,200,fill='yellow',tag='circle')]

speed_x1 = random.randint(-10,10)
speed_y1 = random.randint(-3,3)

speed_x2 = random.randint(-10,10)
speed_y2 = random.randint(-3,3)

speed_x3 = random.randint(-10,10)
speed_y3 = random.randint(-3,3)


while True:


# Each ball needs own initial spped

    
    canvas.move(ball1, speed_x1, speed_y1)
    canvas.move(ball2, speed_x2, speed_y2)
    canvas.move(ball3, speed_x3, speed_y3)
    canvas.after(50)
    canvas.update()

# Prevent balls from leaving screen

# Need to fix them being linked.

    for y in balls:
        coords = canvas.coords(y)
        if coords[0] <= 0:
            if y == ball1:
                speed_x1 = random.randint(0,10)
            elif y == ball2:
                speed_x2 = random.randint(0,10)
            else:
                speed_x3 = random.randint(0,10)
        if coords[1] <= 0:
            if y == ball1:
                speed_y1 = random.randint(0,3)
            elif y == ball2:
                speed_y2 = random.randint(0,3)
            else:
                speed_y3 = random.randint(0,3)
        if coords[2] >= 500:
            if y == ball1:
                speed_x1 = random.randint(-10,0)
            elif y == ball2:
                speed_x2 = random.randint(-10,0)
            else:
                speed_x3 = random.randint(-10,0)
        if coords[3] >= 500:
            if y == ball1:
                speed_y1 = random.randint(-3,0)
            elif y == ball2:
                speed_y2 = random.randint(-3,0)
            else:
                speed_y3 = random.randint(-3,0)
            

# Collision Detection:

# Difficulty with circular and triangular hitboxes
	
    if len(canvas.find_overlapping(10, 10, 100, 100)) > 1:
        print("collision square")
        print(canvas.find_overlapping(0, 0, 500, 500))

# Triangle
    a = [400, 475]
    b = [200, 350]
    c = [400, 150]
