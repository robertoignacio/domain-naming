# import sqlite3

# Description: This script shows how the string was formatted. Will print the first rows of a table in a sqlite database file.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Create a connection to the SQLite database file
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

table = "main_domain_names_table"

# Execute SQL Select statement
cursor.execute(f'''
    SELECT * FROM {table}
''')

# Fetch all the rows
rows = cursor.fetchall()

# Print the rows in terminal
counter = 0

for row in rows:
    if counter < 10:
        print(row)
        counter += 1
    else:
        break

# Close the connection
db_connection.close()