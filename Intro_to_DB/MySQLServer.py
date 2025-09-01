import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "host": "localhost",
    "user": "root",        # replace with your MySQL username
    "password": "Janetwambua@22"  # replace with your MySQL password
}

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create database
    cursor.execute("CREATE DATABASE alxbookstore")
    print("Database 'alxbookstore' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
