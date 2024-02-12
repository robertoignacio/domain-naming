# import sqlite3

# Description: This script prints the first 10 rows of a table in a sqlite database file.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

char_length = cv.char_length
# Table and column names
dn_table = cv.dn_table
dn_col = cv.dn_col
dn_len_table = cv.dn_len_table

all_combinations = cv.all_combinations

# Create a connection to the SQLite database file
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

# Execute SQL Select statement
cursor.execute(f'''
    SELECT * FROM {dn_len_table}
''')

# cursor.execute(f'''
#     SELECT * FROM {all_combinations}
# ''')

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