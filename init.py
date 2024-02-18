import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='kanishk',
        password='ZebraLegs45',
          # Specify the database name
    )
    print("Connection successful")
    worker = mydb.cursor()
    worker.execute("Create database if not exists workers")
    worker.execute("use  workers")
    # Create paygrade table if not exists
    worker.execute("CREATE TABLE IF NOT EXISTS paygrade (grade VARCHAR(20), basic INT, fda INT, vda FLOAT, hr FLOAT, esi FLOAT, pf FLOAT, cater FLOAT, advance INT, other INT)")

    # Create attendance table if not exists
    worker.execute("CREATE TABLE IF NOT EXISTS attendance (token_number VARCHAR(10) PRIMARY KEY, expected INT, actual INT)")

    # Create master table if not exists with modifications
    worker.execute("CREATE TABLE IF NOT EXISTS master (serial_number INT AUTO_INCREMENT PRIMARY KEY, token_number VARCHAR(10), full_name VARCHAR(40), father_name VARCHAR(40), esi_no INT, pf INT, grade VARCHAR(2))")

except mysql.connector.Error as error:
    print(error)

finally:
    pass