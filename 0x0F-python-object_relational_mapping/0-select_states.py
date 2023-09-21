#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        # Connect to the database using command-line arguments
        my_db = MySQLdb.connect(
            host='localhost', user=argv[1], password=argv[2], db=argv[3], port=3306)

        # Create a cursor object to interact with the database
        my_cursor = my_db.cursor()

        # Execute a SELECT query to fetch data
        my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

        # Fetch all the data returned by the query
        my_data = my_cursor.fetchall()

        # Iterate through the fetched data and print each row
        for row in my_data:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and the database connection
        if 'my_cursor' in locals():
            my_cursor.close()
        if 'my_db' in locals():
            my_db.close()
