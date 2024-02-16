import sqlite3
from tqdm import tqdm # progress bar
import uuid # generates a random UUID

# Description: This script reads a file line by line and inserts the data into a sqlite database table.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
tld_s = cv.tld_s

# Table and column names
dn_table = cv.dn_table
dn_col = cv.dn_col

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

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
    CREATE TABLE IF NOT EXISTS {dn_table}
    (id TEXT PRIMARY KEY {dn_col} TEXT) STRICT
''')

# [      dn_table     ]
# [ -id- ] [ -dn_col- ]

# read the file line by line
# input_file = open(f'../inputfiles/dummy.txt', 'r')
input_file = cv.input_file