from tkinter import *
import random

root = Tk()
root.geometry('600x600')
canvas = Canvas(root, height=600, width=600)
canvas.pack()

def ball(self, canvas, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.canvas = canvas
    self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black")

def drawTriangle(x1, y1, x2, y2, x3, y3, color, width):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
    canvas.create_line(x2, y2, x3, y3, fill=color, width=width)
    canvas.create_line(x3, y3, x1, y1, fill=color, width=width)

#Adding Tank
image = PhotoImage(file="C://Users/keno.deary/Desktop/firestorm/tank.png")
canvas.create_image(300,500, image=image)

#Making Ball, Triangle, Line
ball = canvas.create_oval(0,0,32,32,fill="blue", tag='ball')
drawTriangle(300, 475, 200, 150, 400, 150, 'black', 5)
canvas.create_line(0 , 450, 600, 450, fill='black', width=3)


speed_x = random.randint(-10,10)
speed_y = random.randint(-3,3)

count = 0
while True:
    canvas.move('ball', speed_x, speed_y)
    canvas.after(50)
    canvas.update()

    coords = canvas.coords(ball)
	
    if coords[0] <= 0:
        speed_x = random.randint(0,10)
    if coords[1] <= 0:
        speed_y = random.randint(0,3)
    if coords[2] >= 600:
        speed_x = random.randint(-10,0)
    if coords[3] >= 450:
        speed_y = random.randint(-3,0)
    
    if coords[2] > 200 and coords[2] < 400:
        if coords[1] > 150 and coords[1] < 450:    
            print(f'Hit: {count}')
            count += 1
    

ball = ball(290, 290, 310, 310)

root.mainloop()