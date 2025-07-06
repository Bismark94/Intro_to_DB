import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Open connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # replace with your MySQL username
            password='password' # replace with your MySQL password
        )
        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure resources are closed
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    create_database()
