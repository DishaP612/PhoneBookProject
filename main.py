from tkinter import *
from tkinter import messagebox

phonebook = {}

# Functions
def add_contact():
    name = name_entry.get()
    number = number_entry.get()

    if name == "" or number == "":
        messagebox.showwarning("Warning", "Enter Name and Number")
    else:
        phonebook[name] = number
        messagebox.showinfo("Success", "Contact Added")
        clear_fields()
        display_contacts()

def search_contact():
    name = name_entry.get()

    if name in phonebook:
        number_entry.delete(0, END)
        number_entry.insert(0, phonebook[name])
    else:
        messagebox.showerror("Error", "Contact Not Found")

def update_contact():
    name = name_entry.get()
    number = number_entry.get()

    if name in phonebook:
        phonebook[name] = number
        messagebox.showinfo("Updated", "Contact Updated")
        display_contacts()
    else:
        messagebox.showerror("Error", "Contact Not Found")

def delete_contact():
    name = name_entry.get()

    if name in phonebook:
        del phonebook[name]
        messagebox.showinfo("Deleted", "Contact Deleted")
        clear_fields()
        display_contacts()
    else:
        messagebox.showerror("Error", "Contact Not Found")

def display_contacts():
    listbox.delete(0, END)
    for name, number in phonebook.items():
        listbox.insert(END, f"{name}  :  {number}")

def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, number in phonebook.items():
            file.write(name + "," + number + "\n")
    messagebox.showinfo("Saved", "Contacts Saved")

def clear_fields():
    name_entry.delete(0, END)
    number_entry.delete(0, END)

# GUI Window
root = Tk()
root.title("Phone Book Management System")
root.geometry("500x500")
root.configure(bg="#2c3e50")

# Title
title = Label(root, text="Phone Book Manager",
              font=("Helvetica", 20, "bold"),
              bg="#2c3e50", fg="white")
title.pack(pady=10)

# Frame for inputs
frame = Frame(root, bg="#34495e")
frame.pack(pady=10)

Label(frame, text="Name", font=("Arial", 12),
      bg="#34495e", fg="white").grid(row=0, column=0, padx=10, pady=10)

Label(frame, text="Phone Number", font=("Arial", 12),
      bg="#34495e", fg="white").grid(row=1, column=0, padx=10, pady=10)

name_entry = Entry(frame, font=("Arial", 12))
number_entry = Entry(frame, font=("Arial", 12))

name_entry.grid(row=0, column=1, padx=10, pady=10)
number_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons Frame
btn_frame = Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add", width=12, bg="#27ae60", fg="white", command=add_contact).grid(row=0, column=0, padx=5, pady=5)
Button(btn_frame, text="Search", width=12, bg="#2980b9", fg="white", command=search_contact).grid(row=0, column=1, padx=5, pady=5)
Button(btn_frame, text="Update", width=12, bg="#f39c12", fg="white", command=update_contact).grid(row=1, column=0, padx=5, pady=5)
Button(btn_frame, text="Delete", width=12, bg="#c0392b", fg="white", command=delete_contact).grid(row=1, column=1, padx=5, pady=5)
Button(btn_frame, text="Save", width=26, bg="#8e44ad", fg="white", command=save_contacts).grid(row=2, column=0, columnspan=2, pady=5)

# Listbox Frame
list_frame = Frame(root)
list_frame.pack(pady=10)

listbox = Listbox(list_frame, width=50, height=10, font=("Arial", 11))
listbox.pack(side=LEFT)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()