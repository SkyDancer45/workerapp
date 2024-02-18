import tkinter as tk
import mysql.connector

def delete():
    mydb = mysql.connector.connect(
    host='localhost',
    user='kanishk',
    password='ZebraLegs45',
    database='workers'
)
    print("Connection successful")
    worker = mydb.cursor()
    x = entry.get()
    try:
        delete_query = "DELETE FROM master WHERE token_number = %s"
        worker.execute(delete_query, (x,))
        delete_query = "DELETE FROM attendance WHERE token_number = %s"
        worker.execute(delete_query, (x,)) 
        mydb.commit()
        print(f"Record with token number {x} deleted successfully.")
    except mysql.connector.Error as error:
        print(f"Error deleting record: {error}")

    mydb.close()

root = tk.Tk()
root.title('Worker_Deletion')
label=tk.Label(root, text='Enter the token number of the worker you want to fire')
label.pack()
entry = tk.Entry(root)
entry.pack()
del_button = tk.Button(root,text='Delete',command=delete)
del_button.pack()
root.mainloop()

