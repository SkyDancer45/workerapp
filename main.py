import os
import tkinter as tk
root = tk.Tk()
def register():
    os.system('python ~/workerapp/reg.py')
def close():
    root.destroy()
def attendance():
    os.system('python ~/workerapp/attendance.py')
def salary():
    os.system('python ~/workerapp/salary.py')
def delete():
    os.system('python ~/workerapp/del.py')
register_button = tk.Button(root,text = "register",command=register)
register_button.grid(row=1,column=0)
attendance_button = tk.Button(root,text="attendance",command=attendance)
attendance_button.grid(row = 2,column=0)
salary_button = tk.Button(root,text="salary",command=salary)
salary_button.grid(row = 3,column=0)
delete_button = tk.Button(root,text='fire someone',command=delete)
delete_button.grid(row=4,column=0)
close_button = tk.Button(root,text='close',command=close)
close_button.grid(row = 5, column=0)
root.mainloop()
