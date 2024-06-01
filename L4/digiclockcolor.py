# importing whole module
from tkinter import *
from tkinter.ttk import *
import random
# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    color1 = "#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])
    color2 = "#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])
    if random.randint(0, 1):
        lbl.config(foreground=color1)  # Change background color
    else:
        root.config( background=color2)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='orange',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()