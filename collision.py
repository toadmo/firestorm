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
    tri_area = abs((b[0] - a[0])*(c[1] - a[1] - (c[0] - a[0])*(b[1] - a[1])))

    area1 = abs(a[0] - )

    tri_distances = []
    for x in tri_coords
    
    function checkTrianglePoint({points,px,py}) {
  const [point1,point2,point3] = points;
  const [x1,y1] = point1;
  const [x2,y2] = point2;
  const [x3,y3] = point3;
  //Original gross area
  const areaOrig = Math.abs( (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) );

  //Area formed by detection point and triangle vertex
  const area1 = Math.abs( (x1-px)*(y2-py) - (x2-px)*(y1-py) );
  const area2 = Math.abs( (x2-px)*(y3-py) - (x3-px)*(y2-py) );
  const area3 = Math.abs( (x3-px)*(y1-py) - (x1-px)*(y3-py) );
  const areaTotal = area1 + area2 + area3;

  //Allowable value of calculation error
  const buffer = 0.1;
  if (areaTotal >= areaOrig-buffer && areaTotal<= areaOrig+buffer) {
    return true;
  }
  return false;
}


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
