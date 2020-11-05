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

ball1 = canvas.create_oval(100,100,122,122,fill="blue", tag='ball')
ball2 = canvas.create_oval(15,15,47,47,fill="blue", tag='ball')
ball3 = canvas.create_oval(30,30,62,62,fill="blue", tag='ball')

balls = [ball1, ball2, ball3]

shapes = [drawTriangle(400, 475, 200, 350, 400, 150, 'black', 5), drawRectangle(450, 450, 550, 550, 'green', 5), canvas.create_oval(100,100,200,200,fill='yellow',tag='circle')]

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
        if coords[2] >= 1000:
            if y == ball1:
                speed_x1 = random.randint(-10,0)
            elif y == ball2:
                speed_x2 = random.randint(-10,0)
            else:
                speed_x3 = random.randint(-10,0)
        if coords[3] >= 1000:
            if y == ball1:
                speed_y1 = random.randint(-3,0)
            elif y == ball2:
                speed_y2 = random.randint(-3,0)
            else:
                speed_y3 = random.randint(-3,0)
            

# Collision Detection:

# Difficulty with circular and triangular hitboxes
	
    if len(canvas.find_overlapping(450,450,550,550)) > 4:
        print("collision")
        print(canvas.find_overlapping(450,450,550,550))
    

# Instead of touching of first touch, would it be radius distance from center of the ball. 

# If ball within bounding box, then perform calculation with the three lines and making sure it is in that space

# Find extreme positions of both shapes and find the distance from every extreme position to another and find minimum.

# List of data required to have to match targets with firers.
# Must have vs nice to have.

## from sympy import *
#from sympy.geometry import *
#x1, y1, x2, y2, xc, yc = symbols("x1,y1,x2,y2,xc,yc")
#p1 = Point(x1, y1)
#p2 = Point(x2, y2)
#pc = Point(xc, yc)

#line = Line(p1, p2)
#pline = line.perpendicular_line(pc)
#p = line.intersection(pline)[0]
#cse(p, symbols=numbered_symbols("t"))
## 

#([(t0, x1 - x2), (t1, y1 - y2), (t2, x1*y2 - x2*y1), (t3, t0**2 + t1**2)],
# [Point((t0**2*xc + t0*t1*yc - t1*t2)/t3, (t0*t1*xc + t0*t2 + t1**2*yc)/t3)])


#t0 = x1 - x2
#t1 = y1 - y2
#t2 = x1*y2 - x2*y1
#t3 = t0**2 + t1**2

#xp = (t0**2*xc + t0*t1*yc - t1*t2)/t3
#yp = (t0*t1*xc + t0*t2 + t1**2*yc)/t3    
