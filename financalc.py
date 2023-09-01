import tkinter as tk
from tkinter import messagebox

# Import necessary financial functions
import math

# Function to calculate compound interest
def compound_interest(principal, rate, time):
    return principal * (1 + rate/100)**time

# Function to calculate present value
def present_value(future_value, rate, time):
    return future_value / (1 + rate/100)**time

# Function to calculate future value
def future_value(principal, rate, time):
    return principal * (1 + rate/100)**time

# Function to calculate monthly installment for a loan
def loan_monthly_installment(principal, rate, time):
    r = rate / 1200  # Monthly interest rate
    n = time * 12    # Total number of payments
    installment = (principal * r) / (1 - (1 + r)**(-n))
    return installment

# Function to calculate Net Present Value (NPV)
def net_present_value(initial_investment, cashflows, discount_rate):
    npv = -initial_investment
    for t in range(len(cashflows)):
        npv += cashflows[t] / (1 + discount_rate/100)**(t+1)
    return npv

# Function to calculate Internal Rate of Return (IRR) using the Newton-Raphson method
def internal_rate_of_return(initial_investment, cashflows, iterations=100):
    r = 0.1  # Initial guess for IRR
    for i in range(iterations):
        npv = net_present_value(initial_investment, cashflows, r)
        npv_derivative = 0
        for t in range(len(cashflows)):
            npv_derivative -= t * cashflows[t] / (1 + r)**(t+1)
        r = r - npv / npv_derivative
    return r * 100  # Convert to percentage

# Create the main application window
app = tk.Tk()
app.title("Financial Calculator")
app.configure(bg='black')  # Set background color to black

# Function to perform the selected financial calculation
def perform_calculation():
    choice = choice_var.get()
    try:
        if choice == '1':
            principal = float(initial_investment_entry.get())
            rate = float(cashflows_entry.get())
            time = float(discount_rate_entry.get())
            result = compound_interest(principal, rate, time)
            result_label.config(text=f"The future value is: {result:.2f}")
        elif choice == '2':
            future_value = float(initial_investment_entry.get())
            rate = float(cashflows_entry.get())
            time = float(discount_rate_entry.get())
            result = present_value(future_value, rate, time)
            result_label.config(text=f"The present value is: {result:.2f}")
        elif choice == '3':
            principal = float(initial_investment_entry.get())
            rate = float(cashflows_entry.get())
            time = float(discount_rate_entry.get())
            result = future_value(principal, rate, time)
            result_label.config(text=f"The future value is: {result:.2f}")
        elif choice == '4':
            principal = float(initial_investment_entry.get())
            rate = float(cashflows_entry.get())
            time = float(discount_rate_entry.get())
            result = loan_monthly_installment(principal, rate, time)
            result_label.config(text=f"The monthly installment is: {result:.2f}")
        elif choice == '5':
            initial_investment = float(initial_investment_entry.get())
            cashflows = [float(x) for x in cashflows_entry.get().split()]
            discount_rate = float(discount_rate_entry.get())
            result = net_present_value(initial_investment, cashflows, discount_rate)
            result_label.config(text=f"The Net Present Value (NPV) is: {result:.2f}")
        elif choice == '6':
            initial_investment = float(initial_investment_entry.get())
            cashflows = [float(x) for x in cashflows_entry.get().split()]
            result = internal_rate_of_return(initial_investment, cashflows)
            result_label.config(text=f"The Internal Rate of Return (IRR) is: {result:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a variable to hold the choice
choice_var = tk.StringVar()
choice_var.set('1')  # Default choice

# Create a frame for the input fields
input_frame = tk.Frame(app, bg='black')  # Set background color to black
input_frame.pack(padx=10, pady=10)

# Create a label and entry for initial investment
initial_investment_label = tk.Label(input_frame, text="Principal Amount:", fg='white', bg='black')
initial_investment_label.grid(row=0, column=0, padx=5, pady=5)
initial_investment_entry = tk.Entry(input_frame)
initial_investment_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a label and entry for rate
cashflows_label = tk.Label(input_frame, text="Rate (%):", fg='white', bg='black')
cashflows_label.grid(row=1, column=0, padx=5, pady=5)
cashflows_entry = tk.Entry(input_frame)
cashflows_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a label and entry for time
discount_rate_label = tk.Label(input_frame, text="Time (years):", fg='white', bg='black')
discount_rate_label.grid(row=2, column=0, padx=5, pady=5)
discount_rate_entry = tk.Entry(input_frame)
discount_rate_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a button to perform the calculation
calculate_button = tk.Button(input_frame, text="Calculate", command=perform_calculation, bg='blue', fg='white')
calculate_button.grid(row=3, columnspan=2, padx=5, pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="", bg='black', fg='white')
result_label.pack(pady=10)

# Create a label for your information
info_label = tk.Label(app, text="Created by DinethH using Python 3 - 2023", fg="gray", bg='black')
info_label.pack(side=tk.BOTTOM, pady=10)

# Run the GUI main loop
app.mainloop()
