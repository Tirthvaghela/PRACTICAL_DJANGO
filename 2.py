# Create the shown Login Form using
# Tkinter.
# Allow users to enter✔ Username
# and Password
# On clicking✔ Login, check the
# credentials from a MySQL table
# named users
# If valid, display a success message✔
# If invalid, display an error✔
# message
# Add a clickable✔ Register link (no
# functionality needed)

import tkinter as tk
import mysql.connector

root = tk.Tk()

root.title("Show Form")
root.geometry("450x300")

l_1 = tk.Label(root,text="Login Form")
l_1.grid(row=0,column=1)

l_2 = tk.Label(root,text="Username")
l_2.grid(row=1,column=0)

ent_1 = tk.Entry(root)
ent_1.grid(row=1,column=1)

l_3 = tk.Label(root,text="Password")
l_3.grid(row=2,column=0)

ent_2 = tk.Entry(root)
ent_2.grid(row=2,column=1)

btn_chk = tk.Button(root,text="Login",fg="black",bg="grey").grid(row=3,column=1)
btn_chk = tk.Button(root,text="Register",fg="blue",bg="grey").grid(row=4,column=1)

root.mainloop()