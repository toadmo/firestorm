from Tkinter import * as tk

window = tk.Tk()
canvas = Canvas(window, width=100, height=100, background="red")
canvas.pack()

x0 = 45
y0 = 45
x1 = 55
x2 = 55
speed_x = 3
speed_y = 3

ball = canvas.create_oval(x0,y0,x1,y1,fill="blue", tag='ball')
while True:
    canvas.move('ball', speed_x, speed_y)
    canvas.after(30)
    canvas.update

    if x1 >= WIDTH:
        speed_x = -3
    if x0 <= 0:
        speed_x = 3
    if y1 >= HEIGHT:
        speed_y = -3
    if y0 <= 0:
        speed_y = 3
    
    x0 += speed_x
    x1 += speed_x
    y0 += speed_y
    y1 += speed_y

mainloop()