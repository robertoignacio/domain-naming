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



