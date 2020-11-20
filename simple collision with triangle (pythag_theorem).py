from tkinter import *
import random
import math

root = Tk()
root.geometry('500x500')
canvas = Canvas(root, height=500, width=500)
canvas.pack()

ball1 = canvas.create_oval(300,300,332,332,fill="blue", tag='ball')

balls = [ball1]


tri_coords = [200, 200, 100, 400, 300, 400]
point_a = [200, 200]
point_b = [100, 400]
point_c = [300, 400]

canvas.create_polygon(tri_coords, outline='#f11', fill='red', width=2)

def calculate_midpoint(point1, point2):
    side_midpoint = (((point1[0] + point2[0])/2), ((point1[1] + point2[1])/2))
    return side_midpoint

line_a_midpoint = calculate_midpoint(point_a, point_b)
line_b_midpoint = calculate_midpoint(point_b, point_c)
line_c_midpoint = calculate_midpoint(point_a, point_c)


speed_x1 = random.randint(-10,10)
speed_y1 = random.randint(-3,3)

speed_x2 = random.randint(-10,10)
speed_y2 = random.randint(-3,3)

speed_x3 = random.randint(-10,10)
speed_y3 = random.randint(-3,3)

def pythag_dist(x, y):
    dist = math.sqrt((x**2) + (y**2))
    return dist


count = 0
while True:
    canvas.move(ball1, speed_x1, speed_y1)
    # canvas.move(ball2, speed_x2, speed_y2)
    # canvas.move(ball3, speed_x3, speed_y3)
    canvas.after(50)
    canvas.update()


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

    coords = canvas.coords(y)

    ball_x = (coords[0] + coords[2])/2
    ball_y = (coords[1] + coords[3])/2

    #A and B between ball and point on triangle
    point_a_x_ball_point_dist = ball_x - tri_coords[0]
    point_a_y_ball_point_dist = ball_y - tri_coords[1]
    point_b_x_ball_point_dist = ball_x - tri_coords[2]
    point_b_y_ball_point_dist = ball_y - tri_coords[3]
    point_c_x_ball_point_dist = ball_x - tri_coords[4]
    point_c_y_ball_point_dist = ball_y - tri_coords[5]

    #Hypotenuse between point on triangle and ball
    point_a_dist = pythag_dist(point_a_x_ball_point_dist, point_a_y_ball_point_dist)
    point_b_dist = pythag_dist(point_b_x_ball_point_dist, point_b_y_ball_point_dist)
    point_c_dist = pythag_dist(point_c_x_ball_point_dist, point_c_y_ball_point_dist)

    if point_a_dist < 200 and point_b_dist < 200 and point_c_dist < 200:
        print('hit' + str(count))
        count += 1
