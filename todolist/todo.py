from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty!")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    if inputError() == 0:
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()

def delete():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No Task", "No tasks to delete!")
        return

    number = taskNumberField.get().strip()
    if not number.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid task number!")
        return

    task_no = int(number)
    if task_no < 1 or task_no > len(tasks_list):
        messagebox.showerror("Input Error", "Task number out of range!")
        return

    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("ToDo App")
    gui.geometry("300x400")  # Adjusted to give more space

    enterTask = Label(gui, text="Enter Your Task", bg="white", fg="blue", font=("Helvetica", 12))
    enterTaskField = Entry(gui, width=30)
    Submit = Button(gui, text="Submit", fg="white", bg="blue", command=insertTask)
    TextArea = Text(gui, height=10, width=30, font="lucida 12", bg="light blue", fg="black")
    taskNumber = Label(gui, text="Delete Task Number", bg="white", fg="blue", font=("Helvetica", 12))
    taskNumberField = Entry(gui, width=5)
    delete = Button(gui, text="Delete", fg="white", bg="blue", command=delete)
    Exit = Button(gui, text="Exit", fg="white", bg="blue", command=gui.destroy)

    # Grid configuration for centering
    enterTask.grid(row=0, column=0, columnspan=2, pady=10)
    enterTaskField.grid(row=1, column=0, columnspan=2, pady=5)
    Submit.grid(row=2, column=0, columnspan=2, pady=10)
    TextArea.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)
    taskNumber.grid(row=4, column=0, columnspan=2, pady=5)
    taskNumberField.grid(row=5, column=0, columnspan=2, pady=5)
    delete.grid(row=6, column=0, columnspan=2, pady=10)
    Exit.grid(row=7, column=0, columnspan=2, pady=10)

    # Make sure the grid expands properly
    gui.grid_rowconfigure(3, weight=1)
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_columnconfigure(1, weight=1)

    gui.mainloop()
