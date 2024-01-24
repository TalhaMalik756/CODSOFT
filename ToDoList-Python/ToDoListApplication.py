import tkinter
from tkinter import*

root=Tk()
root.title("My To Do List")
root.geometry("400x500+450+50")
root.resizable(False,False)

task_list= []

#Functionality of Add Task Button
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("D:/PROGRAMMING/ToDoList-Python/tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)

#Functionality of Delete Task Button
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("D:/PROGRAMMING/ToDoList-Python/tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

#Textfile to store the list items
def openTaskFile():
    try:
        global task_list
        with open("D:/PROGRAMMING/ToDoList-Python/tasklist.txt", "r") as taskfile:
            tasks=taskfile.readlines()

        for task in  tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END ,task)    
    except:
        file=open('D:/PROGRAMMING/ToDoList-Python/tasklist.txt','w')
        file.close()



#FrontEnd 
#titlebar icon
Image_icon=PhotoImage(file="D:\PROGRAMMING\ToDoList-Python\Images/TitlebarIcon.png")
root.iconphoto(False,Image_icon)

#topbar
TopImage=PhotoImage(file="D:\PROGRAMMING\ToDoList-Python\Images/Titlebar - Black&Gold_01.png")
Label(root,image=TopImage).pack()

#noteicon and heading on the topbar
NoteImage=PhotoImage(file="D:\PROGRAMMING\ToDoList-Python\Images/Clipboard List.png")
Label(root,image=NoteImage,bg="#090804").place(x=30,y=18)
heading=Label(root,text="Tasks To Do", font="Arial 20 bold", fg="#c3bf3c", bg="#090804")
heading.place(x=120,y=16)

#text field and an add button
frame01= Frame(root, width=400, height=28, bg="#f0ff9d")
frame01.place(x=0,y=75)

task=StringVar()
task_entry=Entry(frame01,width=23,font="arial 16",bd=0)
task_entry.place(x=10,y=1)
task_entry.focus()

Addbutton=Button(frame01,text="Add to list",font="arial 11 bold", width=8,bg="black",fg="white", bd=0, command=addTask)
Addbutton.place(x=300,y=0)

#listbox
frame02=Frame(root,bd=3,width=700,height=280,bg="#f0ff9d")
frame02.pack(pady=(38,0))

listbox=Listbox(frame02,font=('arial',12),width=40,height=16,bg="#f0ff9d",fg="black",cursor="hand2",selectbackground="blue")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame02)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete button
DeleteIcon=PhotoImage(file="D:\PROGRAMMING\ToDoList-Python\Images/Delete.png")
Button(root,image=DeleteIcon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()