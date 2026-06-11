import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

def sub_ticket():
    name = name_entry.get().strip()
    pay_meth = pay_method.get()

    if name == "":
        messagebox.showerror("Input Error", "Name cannot be blank.")
        return
    else:
        print(name)

root = tk.Tk ()
root.title("Mini-Movie Fundraiser")
root. geometry ("300x300")

title = ttk. Label (root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold")).grid(row=0, columnspan=2, sticky="n")

ttk. Label (root, text="Name:").grid(row=1, column=0, sticky="w")
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1, column=1)

ttk. Label (root, text="Age:").grid(row=2, column=0, sticky="w")
age_entry = ttk.Entry(root, width=25)
age_entry.grid(row=2, column=1)

ttk. Label (root, text="Payment Methond").grid(row=3, column=0, sticky="w")
pay_method = ttk.Combobox(root, values=["Credit", "Cash"], state="Select")
pay_method.grid (row=3, column =1)

sub_btn = ttk.Button(root, text="Submit Ticket", command=sub_ticket)
sub_btn.grid(row = 4, column=0)

sub_btn = ttk.Button(root, text="Finish")
sub_btn.grid(row = 4, column=1)


root.mainloop()
