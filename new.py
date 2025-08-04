import tkinter as tk
from tkinter import messagebox 

root = tk.Tk()
root.title("Drop down")
root.geometry("400x250")

list1=["Mimu","Tirth","Dhruv","Heet"]

ent_1 = tk.Entry(root)
ent_1.grid(row=1,column=2)

listb= tk.Listbox(root)
listb.grid(row=2,column=2)

# def create():
#     name = ent_1.get()
#     if name :
#         list1.append(name)
#     listb.insert(tk.END,name)
#     ent_1.delete(0,tk.END)
        
def update():
    selected = listb.curselection()
    new_name = ent_1.get()

    if selected and new_name :
        index = selected[0]
        list1[index] = new_name
        listb.delete(index)
        listb.insert(index,new_name)
        ent_1.delete(0,tk.END)
    else :
        messagebox.showinfo("Updated","select a name and enter a new value")

        

# btn = tk.Button(root,text="Submit",command=create).grid(row=3,column=2)
for name in list1 :
    listb.insert(tk.END,name)

btn = tk.Button(root,text="update",command=update).grid(row=4,column=2)


root.mainloop()