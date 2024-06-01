from tkinter import Tk, Label, Listbox, Button, Entry

# Define color options
colors = ["red", "green", "blue", "yellow", "purple"]

window = Tk()
window.title("Color Switcher")

def update_background(event=None):
    """Updates the window background based on the selected color."""
    # Check if any item is selected
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        selected_color = listbox.get(index)
        window.config(background=selected_color)
    else:
        # Handle the case where no item is selected (display message, etc.)
        print("No color selected")
def add_color():
  """Adds a new color from the entry field to the listbox."""
  new_color = color_entry.get()
  if new_color:
    colors.append(new_color.lower())  # Convert to lowercase for consistency
    listbox.insert(listbox.size(), new_color)
    color_entry.delete(0, "end")  # Clear entry field

def remove_color():
  """Removes the selected color from the listbox."""
  selected_index = listbox.curselection()
  if selected_index:
    colors.pop(selected_index[0])
    listbox.delete(selected_index[0])


# Listbox for color selection
listbox = Listbox(window, selectmode="single", exportselection=False)
listbox.config(font=("Arial", 12))
listbox.bind("<<ListboxSelect>>", update_background)  # Bind selection event
for color in colors:
  listbox.insert("end", color)
listbox.pack()

# Label and entry for adding colors
color_label = Label(window, text="Add Color:")
color_label.pack()
color_entry = Entry(window)
color_entry.pack()
add_button = Button(window, text="Add", command=add_color)
add_button.pack()

# Button for removing colors
remove_button = Button(window, text="Remove", command=remove_color)
remove_button.pack()

#update_background()  # Initial background update

window.mainloop()
