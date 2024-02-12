# import sqlite3

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

# Execute a VACUUM command to clean up the database
cursor.execute('VACUUM')

# Close the connection
db_connection.close()