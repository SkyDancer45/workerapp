import tkinter as tk
import mysql.connector

def update_attendance():
    token_number = entry_token.get()

    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='kanishk',
            password='ZebraLegs45',
            database='workers'
        )
        print("Connection successful")
        worker = mydb.cursor()

        # Check if the user exists in the attendance table using token_number
        query = "SELECT * FROM attendance WHERE token_number = %s"
        worker.execute(query, (token_number,))
        user = worker.fetchone()

        if user:
            expected_days = user[1]  # Expected days
            actual_days = user[2]    # Actual days attended

            if actual_days < expected_days:
                # Update the attendance by incrementing the actual days attended by 1
                query = "UPDATE attendance SET actual = actual + 1 WHERE token_number = %s"
                worker.execute(query, (token_number,))
                mydb.commit()
                label_result.config(text="Attendance updated successfully!")
            else:
                label_result.config(text="You have already attended your expected days.")
        else:
            label_result.config(text="User not found in the attendance record.")

        mydb.close()  # Close the database connection

    except mysql.connector.Error as error:
        print(error)

# Create the main window
root = tk.Tk()
root.title("Attendance Login")

# Create Labels
label_token = tk.Label(root, text="Enter your token number:")
label_token.pack()
entry_token = tk.Entry(root)
entry_token.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Button
button_login = tk.Button(root, text="Login", command=update_attendance)
button_login.pack()

root.mainloop()
