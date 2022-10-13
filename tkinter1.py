import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Project 1")
root.geometry("600x400")

name_label = ttk.Label(root,text = "enter your name")
name_label.grid(row=0, column=0)
age_label = ttk.Label(root,text = "enter your age")
age_label.grid(row=1, column=0,sticky='w')
email_label = ttk.Label(root,text = "enter your email")
email_label.grid(row=2, column=0)

name_button = ttk.Button(root, text="submit")


root.mainloop()
