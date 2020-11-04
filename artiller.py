import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width = 300, height = 300, background = "white")
canvas.pack()


triangle = [150,150, 145,145, 145,155]

fa = canvas.create_polygon(triangle, fill = "blue", tag = "fa")
fof = canvas.create_arc(0,0, 300,300, style=tk.PIESLICE, start=315, extent=90,fill='red')

window.mainloop()