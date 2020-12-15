import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("To-do list")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "Warning!", message = "Task cannot be empty.")

def delete_task():
    try:
        task = listbox.curselection()[0]
        listbox.delete(task)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "Task must be selected first.")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox.delete(0, tkinter.END)
        for task in tasks:
            listbox.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "No tasks has been saved.")

def save_task():
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

frame = tkinter.Frame(window)
frame.pack()

listbox = tkinter.Listbox(frame, height = 10, width = 50)
listbox.pack(side = tkinter.LEFT)

scroll = tkinter.Scrollbar(frame)
scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)

listbox.config(yscrollcommand = scroll.set)
scroll.config(command = listbox.yview)

entry = tkinter.Entry(window, width = 52)
entry.pack()

add_btn = tkinter.Button(window, text = "Add task", width = 44, command = add_task)
add_btn.pack()

delete_btn = tkinter.Button(window, text = "Delete task", width = 44, command = delete_task)
delete_btn.pack()

load_btn = tkinter.Button(window, text = "Load task", width = 44, command = load_task)
load_btn.pack()

save_btn = tkinter.Button(window, text = "Save task", width = 44, command = save_task)
save_btn.pack()

window.mainloop()