import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='kanishk',
        password='ZebraLegs45',
        database='workers'
    )
    print("Connection successful")
    worker = mydb.cursor()

    # Create paygrade information
    paygrades_info = [
        ("PG", 2500, 500, 5, 5, 2, 2, 100, 50, 0),
        ("QA", 3000, 500, 5, 5, 2, 2, 120, 60, 0),
        ("VB", 3500, 500, 5, 5, 2, 2, 140, 70, 0),
        ("LY", 4000, 500, 5, 5, 2, 2, 160, 80, 0),
        ("RT", 4500, 500, 5, 5, 2, 2, 180, 90, 0),
        ("XZ", 5000, 500, 5, 5, 2, 2, 200, 100, 0),
        ("NM", 5500, 500, 5, 5, 2, 2, 220, 110, 0),
        ("WS", 6000, 500, 5, 5, 2, 2, 240, 120, 0),
        ("CF", 6500, 500, 5, 5, 2, 2, 260, 130, 0),
        ("JK", 7000, 500, 5, 5, 2, 2, 280, 140, 0),
        ("PL", 7500, 500, 5, 5, 2, 2, 300, 150, 0),
        ("MO", 8000, 500, 5, 5, 2, 2, 320, 160, 0),
        ("UY", 8500, 500, 5, 5, 2, 2, 340, 170, 0),
        ("AZ", 9000, 500, 5, 5, 2, 2, 360, 180, 0),
        ("QS", 9500, 500, 5, 5, 2, 2, 380, 190, 0),
    ]

    # Insert paygrade information into the paygrade table
    insert_query = "INSERT INTO paygrade (grade, basic, fda, vda, hr, esi, pf, cater, advance, other) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    worker.executemany(insert_query, paygrades_info)

    mydb.commit()  # Commit the changes to the database
    mydb.close()   # Close the database connection

    print("Paygrades information inserted successfully!")

except mysql.connector.Error as error:
    print(error)
