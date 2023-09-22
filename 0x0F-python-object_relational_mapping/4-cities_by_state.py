#!/usr/bin/python3
import MySQLdb
import sys

"""
Module that connects a python script to a database
"""

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query to fetch cities
        cursor.execute("""
            SELECT cities.id, cities.name, states.name 
            FROM cities
            JOIN states ON cities.state_id=states.id
            ORDER BY cities.id ASC
        """)

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
