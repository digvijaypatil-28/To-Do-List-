from tkinter import *

#Add Task
def add_task():
    task=task_entry.get()
    if task:
        task_box.insert(END,task)
        task_entry.delete(0,END)
        update_numbering()

#Delete Select Task
def delete_task():
    selected_task=task_box.curselection()
    if selected_task:
        task_box.delete(selected_task)
        update_numbering()

#Clear all Task
def clear_task():
    task_box.delete(0,END)#start from 0 to delete end

#Edit task 
def edit_task():
    selected_task_index=task_box.curselection()
    if selected_task_index:
        task =task_box.get(selected_task_index)
        task = task.split(". ",1)[-1]
        task_entry.delete(0,END)
        task_entry.insert(0,task) 
        task_box.delete(selected_task_index)
        update_numbering()

#Completed Task
def mark_as_done():
    selected_task_index=task_box.curselection()
    if selected_task_index:
        task=task_box.get(selected_task_index) 
        if not task.endswith("✅") :
            task=task.split(". ",1)[-1]
            task_box.delete(selected_task_index)
            task_box.insert(selected_task_index,task + "✅") 
        update_numbering()         

#Assign Numbers
def update_numbering():
    tasks=task_box.get(0,END)
    task_box.delete(0,END)
    for i,task in enumerate(tasks,start=1):
        task = task.split(". ",1)[-1]
        task_box.insert(END,f"{i}. {task}")        

#GUI Setup
window = Tk()
window.title("To Do List ")
window.config(padx=20 , pady=20,bg="#F0F8FF")

#Box for Text Writing
task_entry=Entry(width=25,font=("Parkinsans",14), bg="#FFFFFF",fg="#000000")
task_entry.grid(column=0,row=0,columnspan=4,pady=10)

#To add task button
add_button=Button(text="Add Text",command=add_task,font=("Parkinsans", 12,"bold"),bg="#2196F3", fg="white")
add_button.grid(column=0 ,row=1, padx=5,pady=10)

#To delete task button
delete_button = Button(text="Delete Task",command=delete_task,font=("Parkinsans", 12,"bold"), bg="#F44336", fg="white")
delete_button.grid(column=1,row=1,padx=5,pady=10)

#To clear all the task
clear_button = Button(text="Clear all",command=clear_task,font=("Parkinsans", 12,"bold"), bg="#F44336", fg="white")
clear_button.grid(column=2,row=2 , padx=5,pady=10)

#To edit selected task
edit_button = Button(text="Edit Task",command=edit_task,font=("Parkinsans", 12,"bold"), bg="#F44336", fg="white")
edit_button.grid(column=0,row=2,padx=5,pady=10)

#To Mark as Completed task button
done_button= Button(text="Mark as Done", command=mark_as_done, font=("Parkinsans", 12, "bold"), bg="#2196F3", fg="white")
done_button.grid(column=2,row=1 , padx=5,pady=10)

#Task box to display task
task_box=Listbox(width=40,height=10,font=("Parkinsans", 12),bg="#F5F5F5", fg="#000000", selectbackground="#ADD8E6")
task_box.grid(column=0,row=3,columnspan=3,pady=10)


window.mainloop()