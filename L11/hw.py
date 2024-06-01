from tkinter import *

# Function to calculate percentage
def calculate_percentage():
  try:
    science_marks = int(science_entry.get())
    maths_marks = int(maths_entry.get())
    percentage = (science_marks + maths_marks) / 2
    percentage_entry.delete(0, END)
    percentage_entry.insert(0, str(percentage))
  except ValueError:
    pass  # Handle potential errors during conversion

# Function to clear all fields
def clear_all():
  name_entry.delete(0, END)
  roll_entry.delete(0, END)
  science_entry.delete(0, END)
  maths_entry.delete(0, END)
  percentage_entry.delete(0, END)

# Main window creation
window = Tk()
window.title("Student Information and Marks Logger")

# Title label
title_label = Label(window, text="STUDENT INFORMATION AND MARKS LOGGER", font=("Arial", 16))
title_label.grid(row=0, columnspan=2, padx=10, pady=10)

# Name label and entry
name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = Entry(window)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Roll Number label and entry
roll_label = Label(window, text="Roll Number:")
roll_label.grid(row=2, column=0, padx=5, pady=5)
roll_entry = Entry(window)
roll_entry.grid(row=2, column=1, padx=5, pady=5)

# Marks labels and entries
science_label = Label(window, text="Science Marks:")
science_label.grid(row=3, column=0, padx=5, pady=5)
science_entry = Entry(window)
science_entry.grid(row=3, column=1, padx=5, pady=5)

maths_label = Label(window, text="Maths Marks:")
maths_label.grid(row=4, column=0, padx=5, pady=5)
maths_entry = Entry(window)
maths_entry.grid(row=4, column=1, padx=5, pady=5)

# Percentage label and entry (readonly)
percentage_label = Label(window, text="Percentage:")
percentage_label.grid(row=5, column=0, padx=5, pady=5)
percentage_entry = Entry(window, state='readonly')
percentage_entry.grid(row=5, column=1, padx=5, pady=5)

# Button functions
calculate_button = Button(window, text="Calculate Percentage", command=calculate_percentage)
calculate_button.grid(row=6, columnspan=2, padx=10, pady=10)

edit_button = Button(window, text="Edit", state='disabled')  # Initially disabled
edit_button.grid(row=7, column=0, padx=5, pady=5)

delete_button = Button(window, text="Delete", state='disabled')  # Initially disabled
delete_button.grid(row=7, column=1, padx=5, pady=5)

open_button = Button(window, text="Open")
open_button.grid(row=8, column=0, padx=5, pady=5)

update_add_button = Button(window, text="Update/Add")
update_add_button.grid(row=8, column=1, padx=5, pady=5)

clear_button = Button(window, text="Clear All", command=clear_all)
clear_button.grid(row=9, columnspan=2, padx=10, pady=10)

window.mainloop()
