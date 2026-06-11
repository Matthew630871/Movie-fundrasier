import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#--------------------
#Program Constants
#--------------------

CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

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
    elif new_age < 115:
        return SENIOR_PRICE
    else:
        return -1