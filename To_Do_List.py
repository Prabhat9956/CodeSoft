import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index]
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        tasks[selected_task_index] = f"✔️ {task}"
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, tasks[selected_task_index])
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def search_task():
    query = task_entry.get().strip()
    if query:
        task_listbox.delete(0, tk.END)
        matches = [task for task in tasks if query.lower() in task.lower()]
        for match in matches:
            task_listbox.insert(tk.END, match)
        if not matches:
            messagebox.showinfo("Search Result", "No tasks match your query.")
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

def reset_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Window
root = tk.Tk()
root.title("🧾 To-Do Manager")
root.geometry("800x600")
root.config(bg="#F0F4F8")

tasks = []

# Card Frame
card = tk.Frame(root, bg="white", bd=2, relief="groove")
card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=500)

# Title
tk.Label(card, text="📝 To-Do List", font=("Helvetica", 24, "bold"), bg="white", fg="#2D3436").pack(pady=15)

# Task Entry
entry_frame = tk.Frame(card, bg="white")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=28, bd=2, relief="ridge")
task_entry.pack(side=tk.LEFT, padx=(0, 10))

search_button = tk.Button(entry_frame, text="🔍", command=search_task, bg="#74b9ff", fg="white", font=("Arial", 12), width=4)
search_button.pack(side=tk.LEFT)

# Listbox
task_listbox = tk.Listbox(card, width=40, height=10, font=("Helvetica", 14), bg="#ecf0f1", fg="#2d3436", selectbackground="#0984e3")
task_listbox.pack(pady=10)

# Buttons
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_task, bg="#55efc4", fg="black", font=("Helvetica", 12, "bold"), width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_task, bg="#fab1a0", fg="black", font=("Helvetica", 12, "bold"), width=12).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Complete", command=mark_task_completed, bg="#ffeaa7", fg="black", font=("Helvetica", 12, "bold"), width=12).grid(row=1, column=0, padx=5, pady=10)
tk.Button(btn_frame, text="Reset", command=reset_list, bg="#a29bfe", fg="black", font=("Helvetica", 12, "bold"), width=12).grid(row=1, column=1, padx=5, pady=10)

root.mainloop()
