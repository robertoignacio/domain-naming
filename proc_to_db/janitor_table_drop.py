# import sqlite3

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()

# Before running this script, run 02_what_tables_exist_in_db_and_rows.py to know which table to clean up
# Change the table name to be cleaned up from the imported variables
# Manually change the table to be dropped
drop_table = ""
# ("" is allowed for SQL column names)
# Drop the table! (run the: what_tables_exist_in_db_and_rows.py to see the tables)
cursor.execute(f'DROP TABLE IF EXISTS {drop_table}')
# ('' is allowed for SQL literals)