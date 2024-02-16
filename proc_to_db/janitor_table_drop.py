import sqlite3

import control_vars as cv # From control_vars.py file, values to be set by a Control Panel.

# ---------------------------------

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

# Before running this script, run 02_what_tables_exist_in_db_and_rows.py to know which table to clean up
# Change the table name to be cleaned up from the imported variables
# Manually change the table to be dropped
drop_table = ""
# ("" is allowed for SQL column names)
# Drop the table! (run the: what_tables_exist_in_db_and_rows.py to see the tables)
cursor.execute(f'DROP TABLE IF EXISTS {drop_table}')
# ('' is allowed for SQL literals)