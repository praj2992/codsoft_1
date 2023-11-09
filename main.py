from tkinter import *

scr = Tk()
scr.title("To-Do-List")
scr.geometry("400x650+400+100")
scr.resizable(False, False)

task_list = []


def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('task_list.txt', 'a') as tf:
            tf.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def delete_task():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("task_list.txt", 'w') as tf:
            for task in task_list:
                tf.write(task+"\n")

        listbox.delete(ANCHOR)


def open_task_file():
    try:
        global task_list
        with open("task_list.txt", "r") as tf:
            tasks = tf.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("task_list.txt", "w")
        file.close()


image_icon = PhotoImage(file="images/task.png")
scr.iconphoto(False, image_icon)

top_img = PhotoImage(file="images/topbar.png")
Label(scr, image=top_img).pack()

dock_img = PhotoImage(file="images/dock.png")
Label(scr, image=dock_img, bg="#32405b").place(x=30, y=25)

note_img = PhotoImage(file="images/task.png")
Label(scr, image=note_img, bg="#32405b").place(x=340, y=25)

heading = Label(scr, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = Frame(scr, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=0)

frame1 = Frame(scr, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_task_file()

del_img = PhotoImage(file="images/delete.png")
Button(scr, image=del_img, bd=0, command=delete_task).pack(side=BOTTOM, pady=13)

scr.mainloop()
