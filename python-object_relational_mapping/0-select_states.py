#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get database connection arguments from command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to select all states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Display the results exactly as shown in the example
    for row in rows:
        print(row)

    # Clean up and close connection
    cursor.close()
    db.close()
