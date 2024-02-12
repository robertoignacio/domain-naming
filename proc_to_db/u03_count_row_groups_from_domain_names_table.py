# import sqlite3

# Description : This file counts the number of rows in a table in a SQLite database file.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld

# Table and column names
dn_table = cv.dn_table # domain_names_table (where all the domain names are stored)
dn_col = cv.dn_col # domain_name (the same header name for all tables)


# Create a connection to the SQLite database file
db_connection = cv.db_connection

# ------------------------------------------------
# There is no REVERSE() in SQLite...
# Define a function to find the last occurrence of a substring in a string
def find_last(s, sub):
    return s.rfind(sub) + 1  # +1 to make the position 1-based

# find_last(s, sub) is a Python function that finds the last occurrence of a substring "sub" in a string "s"
# s.rfind(sub) + 1 finds the last occurrence of sub in "s" and adds 1 to make the position 1-based.

# Custom function for sqlite
db_connection.create_function('find_last', 2, find_last)
# ------------------------------------------------

# Create a cursor object
cursor = db_connection.cursor()

# Get the substring up to the last occurrence of {tld} and then get its length
# Execute a SELECT statement to get the number of rows for each character length up to the last occurrence of the TLD
# Execute a SELECT statement to get the number of rows for each character length up to the last occurrence of the TLD
cursor.execute(f'''
    SELECT LENGTH(SUBSTR({dn_col}, 1, find_last({dn_col}, '{tld}') - 1)), COUNT(*)
    FROM {dn_table}
    WHERE {dn_col} LIKE '%{tld}%'
    GROUP BY LENGTH(SUBSTR({dn_col}, 1, find_last({dn_col}, '{tld}') - 1))
''')

# The LIKE statement will search for a specified pattern in a column
# The % wildcard character is used to match zero or more characters

# Fetch all results
results = cursor.fetchall()

# Print each result
for result in results:
    print(f'length: {result[0]}, are registered: {result[1]}')

# Close the connection
db_connection.close()