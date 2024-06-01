import calendar
import tkinter as tk

def showCal():
    fetch_year = int(year_entry.get())
    cal_content = calendar.TextCalendar(calendar.SUNDAY).formatyear(fetch_year)
    cal_label.config(text=cal_content)

root = tk.Tk()
root.title("Calendar")

year_label = tk.Label(root, text="Enter Year:")
year_label.pack()

year_entry = tk.Entry(root)
year_entry.pack()

show_button = tk.Button(root, text="Show Calendar", command=showCal)
show_button.pack()

cal_label = tk.Label(root, text="")
cal_label.pack()

root.mainloop()