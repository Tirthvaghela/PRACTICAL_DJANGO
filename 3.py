#DATABASE CONNECTION WITH TKINTER......

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "",
    database = "user_data"
)

cursor = con.cursor()


    

gen = ["Male", "Female", "Other"]

def show():
    Fullname = E1.get()
    email = E2.get()
    gender = gender_var.get()
    age = E4.get()
    
    
    result = f"Fullname : {Fullname} \n Email : {email} \n gender : {gender} \n Age : {age} \n "
    L5.config(text=result)

    cursor.execute("INSERT INTO user (Fullname,email,gender,age) VALUES (%s,%s,%s,%s)",(Fullname,email,gender,age))
    con.commit()
    print("DATA INSERTED SUCCESSFULLY")

def delete():
    selected = listb.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")
        return

    user_id = listb.get(selected[0]).split(" - ")[0]  # extract id
    cursor.execute("DELETE FROM user WHERE id=%s", (user_id,))
    con.commit()
    messagebox.showinfo("Success", "Record deleted successfully!")
    load_data()

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x250")

# Title
Ras = tk.Label(root, text="Registration Form", justify="center", font=("Arial", 14))
Ras.grid(row=0, column=1, pady=10)

# Full Name
L1 = tk.Label(root, text="Full name:")
L1.grid(row=1, column=0, sticky="e")
E1 = tk.Entry(root)
E1.grid(row=1, column=1)

# Email
L2 = tk.Label(root, text="Email:")
L2.grid(row=2, column=0, sticky="e")
E2 = tk.Entry(root)
E2.grid(row=2, column=1)

# Gender
L3 = tk.Label(root, text="Gender:")
L3.grid(row=3, column=0, sticky="e")
gender_var = tk.StringVar()

r1 = tk.Radiobutton(root, text=gen[0], variable=gender_var, value='Male')
r1.grid(row=3, column=1)
r2 = tk.Radiobutton(root, text=gen[1], variable=gender_var, value='Female')
r2.grid(row=3, column=2)
r3 = tk.Radiobutton(root, text=gen[2], variable=gender_var, value='Other')
r3.grid(row=3, column=3)

# Age
L4 = tk.Label(root, text="Age:")
L4.grid(row=4, column=0, sticky="e")
E4 = tk.Entry(root)
E4.grid(row=4, column=1)
# Submit button
btn = tk.Button(root, text="Insert", fg="white", bg="red", command=show)
btn.grid(row=5, column=1)

# Listbox to display users
listb = tk.Listbox(root, width=40)
listb.grid(row=7, column=0, columnspan=3, pady=10)

# Delete button
del_btn = tk.Button(root, text="Delete", fg="white", bg="blue", command=delete)
del_btn.grid(row=8, column=1)

L5 = tk.Label(root)
L5.grid(row=6, column=0)

def load_data():
    listb.delete(0, tk.END)
    cursor.execute("SELECT id, Fullname FROM user")
    for row in cursor.fetchall():
        listb.insert(tk.END, f"{row[0]} - {row[1]}")

load_data()

root.mainloop()
