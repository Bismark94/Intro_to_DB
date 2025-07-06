import mysql.connector


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

    except mysql.connector.Error as err:
        # Handle connection or execution errors
        print(f"Error: {err}")

    finally:
        # Ensure resources are closed
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass
        try:
            if connection.is_connected():
                connection.close()
        except Exception:
            pass


if __name__ == '__main__':
    create_database()
