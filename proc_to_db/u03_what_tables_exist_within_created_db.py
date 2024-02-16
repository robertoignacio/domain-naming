import sqlite3

# Description: This script prints all the tables in a sqlite database file, column names, and the number of rows in each table

import control_vars as cv # From control_vars.py file, values to be set by a Control Panel.

tld = cv.tld
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# Create or connect to sqlite file db
# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)

# Create a cursor
cursor = db_connection.cursor()

# ------------------------------
# Use the sqlite_master table to get a list of all tables in the database.
# For each table, you can use the PRAGMA table_info statement to get the columns.
# Note that both sqlite_master and PRAGMA table_info are specific to SQLite and won't work with other database engines.
# Use the SELECT COUNT(*) statement to get the row count.

# Get all tables in the database
# Each tuple in the result set contains one element (the table name), so table[0] is the table name.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
all_tables = cursor.fetchall()

# For each table in the database, get the columns and row count
for table in all_tables:
    # Extract the first element from the table tuple.
    table_name = table[0]

    # Get information about a table: the columns
    cursor.execute(f'PRAGMA table_info({table_name});')
    # PRAGMA table_info() returns a list of tuples with information about a column in a table.
    # Each returned tuple contains: cid, name, type, notnull, dflt_value, and pk.
    # column[1] is the name of the column.
    # Get all columns in that table
    columns_of_that_table = cursor.fetchall()
    # Create a list of column names
    column_names = [column[1] for column in columns_of_that_table]
    # Prints the second element of the column tuple

    # Get the row count in the table
    cursor.execute(f'SELECT COUNT(*) FROM {table_name};')
    # Retrieve the first row of the result set returned by the SELECT statement.
    # Is expected to return a single row because the SQL query is using COUNT(*) to get the number of rows in the table.
    row_count = cursor.fetchone()[0]

    # Print the table name, column names, and row count
    print(f'Table: {table_name}: Columns: {column_names}, Rows: {row_count}')    