#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
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

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
