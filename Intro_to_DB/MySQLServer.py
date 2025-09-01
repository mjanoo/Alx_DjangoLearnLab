import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "host": "localhost",
    "user": "root",       # replace with your MySQL username
    "password": "Janetwambua@22"  # replace with your MySQL password
}

try:
    # Connect to MySQL server (not to a specific database yet)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
