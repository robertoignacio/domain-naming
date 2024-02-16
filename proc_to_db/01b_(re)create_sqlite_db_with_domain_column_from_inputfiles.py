import sqlite3
from tqdm import tqdm # progress bar
import uuid # generates a random UUID

# Description: This script creates a sqlite database file from a file that contains domain names.

tld = str('.dev')
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# Dump file to be read, that contains the domain names
input_file = open(f'../inputfiles/icann_tld_{tld_s}_global_list_latest.txt', 'r')

# Create or connect to sqlite file db
# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# ---------------------------------
# (https://www.sqlite.org/stricttables.html)
# With STRICT: the datatype must be one of following: INT, INTEGER, REAL, TEXT, BLOB, ANY (no type coercion)
# Content inserted into the column with a datatype other than ANY must be either a NULL (assuming there is no NOT NULL constraint on the column) or the type specified.
# Columns that are part of the PRIMARY KEY are implicitly NOT NULL.
# An INTEGER PRIMARY KEY column is an alias for the rowid, but an INT PRIMARY KEY column is not.

# https://www.sqlite.org/lang.html
# https://www.sqlite.org/lang_createtable.html
# https://www.sqlite.org/withoutrowid.html
# Create table
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS "domain_names_table"
    (id TEXT PRIMARY KEY "domain_name" TEXT) STRICT
''')

# [  domain_names_table  ]
# [  id  ] [ domain_name ]

# Read the file line by line
