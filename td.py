# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:56:07 2023

@author: shiva
"""


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Define a function to add a new task to the list
def add_task():
    task = task_entry.get()
    start_time = start_entry.get()
    end_time = end_entry_label.get()
    if task:
        task_with_time = f"{task} ({start_time}-{end_time})"
        task_list.insert(tk.END, task_with_time)
        task_entry.delete(0, tk.END)
        start_entry.delete(0, tk.END)
        end_entry_label.delete(0, tk.END)
        
        
# Define a function to delete a task from the list
def delete_task():
    task_index = task_list.curselection()
    if task_index:
        task_list.delete(task_index)

# Create the main window and set its title
root = tk.Tk()
root.title("To-Do List")
root.configure(background="orange")
root.geometry("450x300")


img = Image.open("bck.jpg")
img = img.resize((500, 500), Image.ANTIALIAS)
root.background_image = ImageTk.PhotoImage(img)
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create the task list and add a scrollbar to it
task_list = tk.Listbox(root,bd=5,relief='solid',width=50,justify="center")
task_list.pack(side=tk.LEFT, padx=10, pady=10)
task_list.place(x=10,y=10)


scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Create the task entry and add a button to add new tasks
task_name_label = tk.Label(root, text="Task Name:",font=('Times','10', 'italic'),relief='solid',bd=1)
task_name_label.place(x=10, y=190)


task_entry = tk.Entry(root, width=30)
task_entry.place(x=100, y=190)


start_entry_label = tk.Label(root, text="start_time",font=('Times','10', 'italic'),relief='solid',bd=1)
start_entry_label.place(x=10, y=230)

start_entry =tk.Entry(root, width=10)
start_entry.place(x=80, y=230)


end_entry_label = tk.Label(root, text="end time:",font=('Times','10', 'italic'),relief='solid',bd=1)
end_entry_label.place(x=160, y=230)

end_entry_label =tk.Entry(root, width=10)
end_entry_label.place(x=220, y=230)


add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=10)
add_button.place(x=350, y=50)

# Add a button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(padx=10, pady=10)
delete_button.place(x=350, y=80)


#add_button.pack(side=tk.LEFT, padx=10, pady=10)


root.resizable(False,False)
# Start the main loop
root.mainloop()
