#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print("({}, '{}')".format(state[0], state[1]))

    # Close the cursor and database connection
    cursor.close()
    db.close()
