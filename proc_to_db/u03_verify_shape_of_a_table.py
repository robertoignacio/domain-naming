import sqlite3

# Description: This script shows how the string was formatted. Will print the first rows of a table in a sqlite database file.

import control_vars as cv # From control_vars.py file, values to be set by a Control Panel.

tld = cv.tld
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# ---------------------------------
# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# ---------------------------------
table = "all_comb_length_2"

# Execute SQL Select statement
cursor.execute(f'''
    SELECT * FROM {table}
''')

# Fetch all the rows
rows = cursor.fetchall()

# Print the rows in terminal
counter = 0

for row in rows:
    if counter < 100:
        print(row)
        counter += 1
    else:
        break

# Close the connection
db_connection.close()