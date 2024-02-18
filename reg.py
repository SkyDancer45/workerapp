import tkinter as tk
import mysql.connector
import calendar
from datetime import datetime

def calculate_business_days():
    # Calculate the total business days in the current month (assuming Monday to Friday)
    today = datetime.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    business_days = sum(1 for day in range(1, num_days + 1) if calendar.weekday(today.year, today.month, day) < 5)
    return business_days

def save_to_database():
    # Get the values from the entry fields
    token_number = entry_token_number.get()
    full_name = entry_full_name.get()
    father_name = entry_father_name.get()
    esi_no = entry_esi_no.get()
    pf = entry_pf.get()
    grade = entry_grade.get()

    # Basic input validation
    if not token_number.isdigit() or len(token_number) != 10:
        print("Please enter a valid 10-digit token number.")
        return

    try:
        float(pf)
        # Additional validations for other fields can be added as needed

        mydb = mysql.connector.connect(
            host='localhost',
            user='kanishk',
            password='ZebraLegs45',
            database='workers'
        )
        print("Connection successful")
        worker = mydb.cursor()

        # Calculate expected days based on the current month's business days
        expected_days = calculate_business_days()

        # Insert the worker information into the master table
        insert_query = "INSERT INTO master (token_number, full_name, father_name, esi_no, pf, grade) VALUES (%s, %s, %s, %s, %s, %s)"
        worker.execute(insert_query, (token_number, full_name, father_name, esi_no, pf, grade))

        # Insert the worker information into the attendance table with expected days as calculated
        insert_attendance_query = "INSERT INTO attendance (token_number, expected, actual) VALUES (%s, %s, 0)"
        worker.execute(insert_attendance_query, (token_number, expected_days))

        mydb.commit()  # Commit the changes to the database
        mydb.close()   # Close the database connection
        print("Data inserted successfully!")

        # Clear the entry fields after successful data insertion
        entry_token_number.delete(0, tk.END)
        entry_full_name.delete(0, tk.END)
        entry_father_name.delete(0, tk.END)
        entry_esi_no.delete(0, tk.END)
        entry_pf.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    except mysql.connector.Error as error:
        print(error)
    except ValueError:
        print("Please enter a valid numeric value for PF.")

def clear_entries():
    entry_token_number.delete(0, tk.END)
    entry_full_name.delete(0, tk.END)
    entry_father_name.delete(0, tk.END)
    entry_esi_no.delete(0, tk.END)
    entry_pf.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

def close_window():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Worker Registration")

# Create Labels
label_token_number = tk.Label(root, text="Token Number:")
label_token_number.pack()
entry_token_number = tk.Entry(root)
entry_token_number.pack()

label_full_name = tk.Label(root, text="Full Name:")
label_full_name.pack()
entry_full_name = tk.Entry(root)
entry_full_name.pack()

label_father_name = tk.Label(root, text="Father's Name:")
label_father_name.pack()
entry_father_name = tk.Entry(root)
entry_father_name.pack()

label_esi_no = tk.Label(root, text="ESI Number:")
label_esi_no.pack()
entry_esi_no = tk.Entry(root)
entry_esi_no.pack()

label_pf = tk.Label(root, text="PF:")
label_pf.pack()
entry_pf = tk.Entry(root)
entry_pf.pack()

label_grade = tk.Label(root, text="Grade:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

# Buttons
button_save = tk.Button(root, text="Save", command=save_to_database)
button_save.pack()

button_clear = tk.Button(root, text="Clear", command=clear_entries)
button_clear.pack()

# Add Close button
button_close = tk.Button(root, text="Close", command=close_window)
button_close.pack()

root.mainloop()
