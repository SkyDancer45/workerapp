
import tkinter as tk
import mysql.connector
from tkinter import ttk

def calculate_total_salary():
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

        # Fetch the user's details
        user_query = "SELECT full_name, token_number FROM master WHERE token_number = %s"
        worker.execute(user_query, (token_number,))
        user_data = worker.fetchone()

        if user_data:
            full_name = user_data[0]  # Full Name
            token_number = user_data[1]  # Token Number

            # Fetch the user's attendance details
            attendance_query = "SELECT expected, actual FROM attendance WHERE token_number = %s"
            worker.execute(attendance_query, (token_number,))
            attendance_data = worker.fetchone()

            if attendance_data:
                expected_days = attendance_data[0]  # Expected days
                actual_days = attendance_data[1]    # Actual days attended

                # Fetch paygrade details
                paygrade_query = "SELECT * FROM paygrade WHERE grade = (SELECT grade FROM master WHERE token_number = %s)"
                worker.execute(paygrade_query, (token_number,))
                paygrade_data = worker.fetchone()

                if paygrade_data:
                    basic_salary = paygrade_data[1]  # Basic salary
                    fda_amount = paygrade_data[2]    # FDA amount
                    vda_amount = paygrade_data[3]    # VDA amount
                    hr_percentage = paygrade_data[4] # HR percentage
                    esi_percentage = paygrade_data[5] # ESI percentage
                    pf_percentage = paygrade_data[6] # PF percentage
                    cater_amount = paygrade_data[7]  # Catering amount
                    advance_amount = paygrade_data[8] # Advance amount
                    other_amount = paygrade_data[9]  # Other amount

                    # Calculate total salary based on days worked
                    total_salary = ((basic_salary + fda_amount + vda_amount) * actual_days) / expected_days

                    # Calculate amounts based on percentages
                    hr_deduction_amount = (basic_salary + fda_amount + vda_amount) * hr_percentage / 100
                    esi_deduction_amount = total_salary * esi_percentage / 100
                    pf_deduction_amount = total_salary * pf_percentage / 100

                    # Calculate final salary after all deductions
                    final_salary = total_salary - (hr_deduction_amount + esi_deduction_amount + pf_deduction_amount + advance_amount + other_amount + cater_amount)

                    # Create a Tkinter window for displaying the table
                    table_window = tk.Tk()
                    table_window.title("Salary Details")

                    # Create Labels and show data horizontally
                    labels = [
                        f"Token Number: {token_number}",
                        f"Full Name: {full_name}",
                        f"Total Salary: {final_salary}",
                        f"Basic Salary: {basic_salary}",
                        f"FDA Amount: {fda_amount}",
                        f"VDA Amount: {vda_amount}",
                        f"HR Deduction: {hr_deduction_amount}",
                        f"ESI Deduction: {esi_deduction_amount}",
                        f"PF Deduction: {pf_deduction_amount}",
                        f"Advance Amount: {advance_amount}",
                        f"Other Amount: {other_amount}",
                        f"Catering Deduction: {cater_amount}"
                    ]

                    # Create Labels in a grid layout
                    for i, label_text in enumerate(labels):
                        label = tk.Label(table_window, text=label_text)
                        label.grid(row=i // 2, column=i % 2, sticky="w")

                    table_window.mainloop()

                else:
                    label_result.config(text="Paygrade information not found.")
            else:
                label_result.config(text="Attendance record not found.")
        else:
            label_result.config(text="User not found.")

        mydb.close()  # Close the database connection

    except mysql.connector.Error as error:
        print(error)

# Create the main window
root = tk.Tk()
root.title("Calculate Total Salary")

# Create Labels and Entry
label_token = tk.Label(root, text="Enter user's token number:")
label_token.pack()
entry_token = tk.Entry(root)
entry_token.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Button
button_calculate = tk.Button(root, text="Show Salary Details", command=calculate_total_salary)
button_calculate.pack()

root.mainloop()

