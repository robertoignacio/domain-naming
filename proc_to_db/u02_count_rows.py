# import sqlite3

# Description : This file counts the number of rows in a table in a SQLite database file.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
tld_s = cv.tld_s
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
    SELECT COUNT({dn_col}) FROM {dn_len_table}
''')

# cursor.execute(f'''
#     SELECT COUNT(combination) FROM {all_combinations}
# ''')

# Fetch the count result
# Index the tuple returned by fetchone() to get the count
num_rows = cursor.fetchone()[0]

# Print to terminal
print(f'The number of rows is {num_rows}.')

# Close the connection
db_connection.close()