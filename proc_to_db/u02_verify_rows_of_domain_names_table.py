# import sqlite3

# Description : This file counts the number of rows in the main table "domain_names_table".

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Table and column names
dn_table = cv.dn_table
dn_col = cv.dn_col

# Create a connection to the SQLite database file
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

# Execute SQL Select statement
cursor.execute(f'''
    SELECT COUNT({dn_col}) FROM {dn_table}
''')

# Fetch the count result
# Index the tuple returned by fetchone() to get the count
num_rows = cursor.fetchone()[0]

# Print to terminal
print(f'The number of rows is {num_rows}.')

# Close the connection
db_connection.close()