from tkinter import Tk, Label, Entry, Button

def convert_currency():
 
  try:
    # Get user input
    source_amount = float(source_currency_entry.get())

    # Assuming source currency is always INR (Indian Rupee)
    source_currency = "INR"
    target_currency = "USD"  # Target currency is US Dollar

    # Conversion logic (replace with your preferred method)
    # Option 1: Manual conversion rate (for demonstration purposes)
    conversion_rate = 0.013  # Hypothetical conversion rate (replace with actual rate)
    converted_amount = source_amount * conversion_rate

    # Option 2: Use an external currency conversion API (refer to previous explanation)
    # converted_amount = fetch_conversion_from_api(source_amount, source_currency, target_currency)

    # Display converted amount
    target_currency_entry.config(state="normal")  # Enable target entry
    target_currency_entry.delete(0, "end")  # Clear previous value
    target_currency_entry.insert(0, converted_amount)  # Display converted amount
    target_currency_entry.config(state="disabled")  # Disable target entry again
  except ValueError:
    # Handle invalid user input
    print("Invalid input. Please enter a number.")
  pass

# Create the main window
window = Tk()
window.title("Currency Converter")

# Create the currency converter label
currency_converter_label = Label(window, text="Currency Converter", font=("Arial", 16))
currency_converter_label.grid(row=0, columnspan=3, padx=10, pady=10)

# Create the source currency label
source_currency_label = Label(window, text="Source Currency amount (Rs.)")
source_currency_label.grid(row=1, column=0, padx=10, pady=10)

# Create the source currency entry field
source_currency_entry = Entry(window, width=15)
source_currency_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the target currency label
target_currency_label = Label(window, text="Target Currency amount ($)")
target_currency_label.grid(row=1, column=2, padx=10, pady=10)

# Create the target currency entry field (disabled for now)
target_currency_entry = Entry(window, width=15, state="disabled")
target_currency_entry.grid(row=1, column=3, padx=10, pady=10)

# Create the convert button
convert_button = Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=2, columnspan=3, padx=10, pady=10)

# Run the main loop
window.mainloop()