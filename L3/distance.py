from tkinter import Tk, Label, Entry, Button

def calculate_distance():
  try:
    # Get user input
    time = float(time_entry.get())
    speed = float(speed_entry.get())

    # Calculate distance
    distance = time * speed

    # Display result
    result_label.config(text=f"Distance covered: {distance:.2f} kilometers")
  except ValueError:
    # Handle invalid user input
    result_label.config(text="Invalid input. Please enter numbers only.")

# Create the main window
window = Tk()
window.title("Distance Calculator")

# Create labels for time and speed
time_label = Label(window, text="Time (hours):")
time_label.grid(row=0, column=0, padx=10, pady=10)

speed_label = Label(window, text="Speed (km/hr):")
speed_label.grid(row=1, column=0, padx=10, pady=10)

# Create entry fields for time and speed
time_entry = Entry(window, width=10)
time_entry.grid(row=0, column=1, padx=10, pady=10)

speed_entry = Entry(window, width=10)
speed_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to calculate distance
calculate_button = Button(window, text="Calculate Distance", command=calculate_distance)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_label = Label(window, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main loop
window.mainloop()