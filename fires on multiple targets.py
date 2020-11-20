import random
import math
from tkinter import *
import time
import numpy
import cmath

root = Tk()
root.geometry('500x500')
canvas = Canvas(root, height=500, width=500)
canvas.pack()

class shape(object):
    def __init__(self, shape_type):
        self.type = shape_type
    def print_shape(self):
        print(f"This is a {self.type}")
    def point_inside_shape(self, x_pos, y_pos):
        x = x
    def line_collision(self, a, b, c):
        raise NotImplementedError("This function needs to be implemented.")

# Circle Class

class circle(shape):
    def __init__(self, x_p, y_p, vel_x, vel_y, rad):
        super().__init__("circle")
        self.x_pos = x_p
        self.y_pos = y_p
        self.x_velocity = vel_x
        self.y_velocity = vel_y
        self.radius = rad
    def print_shape(self):
        super(circle, self).print_shape()
        print(f"It is at postion ({self.x_pos},{self.y_pos}) and has a radius of {self.radius}.")
    def point_inside_shape(self, x_coord, y_coord):
        distance = math.sqrt((x_coord - self.x_pos)**2 + (y_coord - self.y_pos)**2)
        return distance < self.radius
    def line_collision(self, a, b, c):
        dist = ((abs(a * self.x_pos + b * self.y_pos + c)) / math.sqrt(a * a + b * b)) 
        if (self.radius == dist): 
            print("That line just touches the circle") 
        elif (self.radius > dist): 
            print("That line goes through the circle") 
        else: 
            print("That line does not touch the circle.") 
    def get_location_x(self):
        return self.x_pos
    def get_location_y(self):
        return self.y_pos
    def changeLocation(self):
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity
    def create_shot(self):
        canvas.create_circle

# Rectangle Class

class rectangle(shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def point_inside_shape(self, p_x, p_y):
        return p_x > self.x1 and p_x < self.x2 and p_y > self.y1 and p_y < self.y2
    def print_shape(self):
        print(f"My corners are at ({self.x1},{self.y1}), ({self.x1},{self.y2}), ({self.x2},{self.y2}), ({self.x2},{self.y1})")
    def create_target(self):
        canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill='blue')
    def midpoint(self):
        return [(self.x1+self.x2)/2,(self.y1+self.y2)/2]
    def t_r(self):
        return [self.x1, self.y1]
    def b_l(self):
        return [self.x2, self.y2]


# Triangle Class 

def cross(a, b):
    return [a[1] * b[2] - b[1] * a[2], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

class triangle(shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def point_inside_shape(self, p_x, p_y):
        ap = [self.x1 - p_x, self.y1 - p_y, 0]
        ab = [self.x1 - self.x2, self.y1 - self.y2, 0]
        bp = [self.x2 - p_x, self.y2 - p_y, 0]
        bc = [self.x2 - self.x3, self.y2 - self.y3, 0]
        cp = [self.x3 - p_x, self.y3 - p_y, 0]
        ca = [self.x3 - self.x1, self.y3 - self.y1, 0]
        a = cross(ap, ab)
        b = cross(bp, bc)
        c = cross(cp, ca)
        return ((a[2] > 0 and b[2] > 0 and c[2] > 0) or (a[2] < 0 and b[2] < 0 and c[2] < 0))
    def print_shape(self):
        print(f"My corners are at ({self.x1},{self.y1}), ({self.x2},{self.y2}), ({self.x3},{self.y3}).") 

# Coordinates Being Established

artillery_coords = [250,50,230,20,270,20] 

# Creating Shapes


def drawTriangle(x1, y1, x2, y2, x3, y3, color, width):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=width, tag='line')
    canvas.create_line(x2, y2, x3, y3, fill=color, width=width, tag='line')
    canvas.create_line(x3, y3, x1, y1, fill=color, width=width, tag='line')

drawTriangle(artillery_coords[0],artillery_coords[1],artillery_coords[2],artillery_coords[3],artillery_coords[4],artillery_coords[5],'blue',1)


def drawRectangle(x1,y1,x2,y2, color, width):
    canvas.create_line(x1,y1,x1,y2, fill=color, width=width)
    canvas.create_line(x1,y1,x2,y1, fill=color, width=width)
    canvas.create_line(x1,y2,x2,y2, fill=color, width=width)
    canvas.create_line(x2,y1,x2,y2, fill=color, width=width)

target_list = []
hit = []
for _ in range(4):
    x = random.randint(0, 500)
    y = random.randint(100, 500)
    target_list.append(rectangle(x,y,x-20, y-20))
    rectangle(x,y,x-20, y-20).create_target()
    hit.append(False)
    
# Sort the List Left to Right

sort = []

for x in target_list:
    sort.append(x.t_r()[0])
    sort.sort()

for x in range(0,4):
    for y in range(0,4):
        if sort[x] == target_list[y].t_r()[0]:
            sort[x] = target_list[y]

# Rotate

def rotate_x(x,y):
    s = math.sin(angle)
    c = math.cos(angle)
    x -= 250
    y -= 20
    xnew = x*c - y*s
    ynew = x*s + y*c
    return xnew+250

def rotate_y(x,y):
    s = math.sin(angle)
    c = math.cos(angle)
    x -= 250
    y -= 20
    xnew = x*c - y*s
    ynew = x*s + y*c
    return ynew+20

# Collision Detection

for x in range(0,4):
    if hit[x] == False:
        vel_x = (sort[x].midpoint()[0] - 250) / 100
        vel_y = (sort[x].midpoint()[1] - 35) / 100
        shot = circle(250,35,vel_x,vel_y,5)
        shot2 = canvas.create_oval(245,30,255,40,fill='yellow',tag='circle')

        # Angle
 

        vector1 = (artillery_coords[0] - (artillery_coords[2]+artillery_coords[4])/2, artillery_coords[1] - (artillery_coords[3]+artillery_coords[5])/2)
        vector2 = (sort[x].midpoint()[0] - (artillery_coords[2]+artillery_coords[4])/2, sort[x].midpoint()[1] - (artillery_coords[3]+artillery_coords[5])/2)

        angle = math.acos(numpy.dot(vector1, vector2)/(numpy.linalg.norm(vector1)*numpy.linalg.norm(vector2)))
        
        counter = 0
        
        while counter != 4:
            tmp_x = artillery_coords[counter]
            tmp_y = artillery_coords[counter + 1]
            artillery_coords[counter] = rotate_x(tmp_x,tmp_y)
            artillery_coords[counter + 1] = rotate_y(tmp_x,tmp_y)
            counter += 2

        canvas.delete('line')
        arti = drawTriangle(artillery_coords[0],artillery_coords[1],artillery_coords[2],artillery_coords[3],artillery_coords[4],artillery_coords[5],'blue',1)

        while len(canvas.find_overlapping(sort[x].t_r()[0], sort[x].t_r()[1], sort[x].b_l()[0], sort[x].b_l()[1])) < 2:
            shot.changeLocation()
            canvas.move(shot2, vel_x, vel_y)
            canvas.after(50)
            canvas.update()
