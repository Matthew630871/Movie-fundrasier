import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#--------------------
#Program Constants
#--------------------

MAX_TICKETS = 5  #Set to 5 for testing. Later set to 150
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
PAYMENT_TYPES = ('cash','credit')

#Data List
all_names = []
all_ticket_costs = []
all_surcharges = []

tickets_sold = 0

def check_age(age):
    # This checks that Users inputed data is valid.
    # Age should be higher than 12, and lower than 114.

    try: 
        new_age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be an integer.")
        return False

    if new_age < 12: 
        messagebox.showerror("Error", "This customer is too young.")
        return -1
    elif new_age < 16:
        return CHILD_PRICE
    elif new_age < 65:
        return ADULT_PRICE
    else:
        return SENIOR_PRICE


def sub_ticket():
    name = name_entry.get().strip()
    pay_meth = pay_method.get()
    age = age_entry.get().strip()

    if name == "":
        messagebox.showerror("Input Error", "Name cannot be blank.")
        return

    ticket_price = check_age(age)

    if ticket_price == -1:
        return

    all_names.append(name)
    all_ticket_costs.append(ticket_price)

    if pay_method == PAYMENT_TYPES[0]:
        all_surcharges.append(0)
    else:
        all_surcharges.append(CREDIT_SURCHARGE)


root = tk.Tk()
root.title("Mini-Movie Fundraiser")
root.geometry("300x300")

title = ttk.Label(root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold"))
title.grid(row=0, columnspan=2, sticky="n")

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="w")
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Age:").grid(row=2, column=0, sticky="w")
age_entry = ttk.Entry(root, width=25)
age_entry.grid(row=2, column=1)

ttk.Label(root, text="Payment Method").grid(row=3, column=0, sticky="w")
pay_method = ttk.Combobox(root, values=["Credit", "Cash"], state="readonly")
pay_method.grid(row=3, column=1)

sub_btn = ttk.Button(root, text="Submit Ticket", command=sub_ticket)
sub_btn.grid(row=4, column=0)

finish_btn = ttk.Button(root, text="Finish")
finish_btn.grid(row=4, column=1)

root.mainloop()
