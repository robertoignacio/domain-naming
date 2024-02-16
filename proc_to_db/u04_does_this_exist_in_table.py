import sqlite3

# Description: This file is used to check if a domain name exists in the table.

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

value_to_find = "aaaa"

# Get all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
all_tables = cursor.fetchall()

# For each table, check each column for the value
for table in all_tables:
    table_name = table[0]

    # Get all columns in the table
    cursor.execute(f'PRAGMA table_info({table_name});')
    all_columns = cursor.fetchall()

    for column in all_columns:
        column_name = column[1]

        # Check if the value exists in the column
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?", (value_to_find,))
        count = cursor.fetchone()[0]

        if count > 0:
            print(f'Value found in table: {table_name} [column: {column_name}]')