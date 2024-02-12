# import sqlite3

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

drop_table = ''

# Drop the table! (run the: what_tables_exist_in_db_and_rows.py to see the tables)
cursor.execute(f'DROP TABLE IF EXISTS {drop_table}')