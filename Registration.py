import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Try connecting to database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # your password
        database="user_data"  # your database name
    )
    cursor = conn.cursor()
    db_connected = True
except mysql.connector.Error as err:
    db_connected = False
    messagebox.showerror("Database Error", f"Error: {err}")

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
pass_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
python_var = tk.IntVar()
java_var = tk.IntVar()
cpp_var = tk.IntVar()
country_var = tk.StringVar()

# Functions
def submit_form():
    if not db_connected:
        messagebox.showerror("Error", "Database is not connected!")
        return

    name = name_var.get().strip()
    email = email_var.get().strip()
    password = pass_var.get().strip()
    age = age_var.get().strip()
    gender = gender_var.get()
    skills = []
    if python_var.get(): skills.append("Python")
    if java_var.get(): skills.append("Java")
    if cpp_var.get(): skills.append("C++")
    country = country_var.get()

    if not (name and email and password and age and gender and country != "Select"):
        messagebox.showerror("Error", "Please fill all required fields!")
        return

    skills_str = ", ".join(skills)
    try:
        sql = """INSERT INTO users 
                 (name, email, password, age, gender, skills, country) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (name, email, password, age, gender, skills_str, country)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        reset_form()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def reset_form():
    name_var.set("")
    email_var.set("")
    pass_var.set("")
    age_var.set("")
    gender_var.set("")
    python_var.set(0)
    java_var.set(0)
    cpp_var.set(0)
    country_var.set("Select")

# Widgets
tk.Label(root, text="Registration Form", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Name:").grid(row=1, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=name_var).grid(row=1, column=1, padx=10)
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10)
tk.Label(root, text="Password:").grid(row=3, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=pass_var, show="*").grid(row=3, column=1, padx=10)
tk.Label(root, text="Age:").grid(row=4, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=age_var).grid(row=4, column=1, padx=10)
tk.Label(root, text="Gender:").grid(row=5, column=0, sticky="w", padx=10)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=5, column=1)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=5, column=1, sticky="e")
tk.Label(root, text="Skills:").grid(row=6, column=0, sticky="w", padx=10)
tk.Checkbutton(root, text="Python", variable=python_var).grid(row=6, column=1, sticky="w")
tk.Checkbutton(root, text="Java", variable=java_var).grid(row=6, column=1)
tk.Checkbutton(root, text="C++", variable=cpp_var).grid(row=6, column=1, sticky="e")
tk.Label(root, text="Country:").grid(row=7, column=0, sticky="w", padx=10)
countries = ["Select", "India", "USA", "UK", "Canada"]
country_var.set("Select")
tk.OptionMenu(root, country_var, *countries).grid(row=7, column=1, padx=10)
tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white").grid(row=8, column=0, pady=10)
tk.Button(root, text="Reset", command=reset_form, bg="red", fg="white").grid(row=8, column=1, pady=10)

root.mainloop()
