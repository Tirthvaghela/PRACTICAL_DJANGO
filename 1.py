import tkinter as tk
from tkinter import *
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user = "php",
    password = "php",
    database = "php_db"
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

L5 = tk.Label(root)
L5.grid(row=6, column=0)

root.mainloop()