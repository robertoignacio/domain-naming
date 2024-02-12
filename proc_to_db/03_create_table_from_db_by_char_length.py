# import sqlite3

# Description: This script creates a new table for char_legth.tld domain names

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
tld_s = cv.tld_s
char_length = cv.char_length
# Table and column names
dn_table = cv.dn_table
dn_col = cv.dn_col
dn_len_table = cv.dn_len_table

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# Create a new table with rows where the character length until the TLD is equal to char_length
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {dn_len_table} AS
    SELECT * FROM {dn_table}
    WHERE INSTR({dn_col}, '{tld}') - 1 = {char_length}
''')

# Commit your changes and close the connection
db_connection.commit()
db_connection.close()