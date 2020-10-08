import Tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Tkinter Starting Point")
greeting.pack() # makes window as small as possible while including whatever was added

label = tk.label(
    text="Hi",
    foreground="white", # can use fg instead
    background="#34A2FE", # bg
    width = 10,
    height = 10
)

window.mainloop()

# Widget Classes:
# Label - Widget used to display text on screen
# Button - Can contain text and can perform action when clicked
# Entry - Allows a single line of entered text
# Text - Entry of multiple lines
# Frame - Rectangular region that groups related widgets or provides padding between widgets
