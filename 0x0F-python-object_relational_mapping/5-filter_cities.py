#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create SQL query with parameterized query
    sql_query = (
        "SELECT GROUP_CONCAT(name SEPARATOR ', ') "
        "FROM cities "
        "WHERE state_id = (SELECT id FROM states WHERE name = %s) "
        "ORDER BY id ASC"
    )

    # Execute SQL query with state_name as parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print the results
    if result:
        print(result)
    else:
        print("")

    # Close the cursor and database connection
    cursor.close()
    db.close()
