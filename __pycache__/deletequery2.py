import mysql.connector

try:
    # MySQL se connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",     # jo password config.inc.php me diya tha
        database="school"
    )

    cursor = mydb.cursor()

    # User se st_id lo jise delete karna hai
    st_id = input("Enter student ID to delete: ")

    # Query execute karo
    query = "DELETE FROM students WHERE st_id = %s"
    cursor.execute(query, (st_id,))

    mydb.commit()  # Changes save karo

    # Feedback do
    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("No student found with this ID.")

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    # Close connection
    if mydb.is_connected():
        cursor.close()
        mydb.close()