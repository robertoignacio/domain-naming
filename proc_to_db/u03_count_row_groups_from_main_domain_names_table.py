import sqlite3

# Description : This script prints all domain name lengths within the domain_names_table, each with the number of registered domain names of that length.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
tld_s = str(tld.lstrip('.'))

# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)

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

dn_table = "main_domain_names_table"
dn_col = "domain_name"

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