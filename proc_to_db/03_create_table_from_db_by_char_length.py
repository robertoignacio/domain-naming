import sqlite3
import control_vars as cv

# Description: This script creates a new table for char_legth.tld domain names

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file

tld = str('.dev')
char_length = int(2)

# Table and column names
dn_table = str('domain_names_table')
dn_col = str('domain_name')
dn_len_table = f'domain_names_length_{char_length}'

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# Create a new table
cursor.execute(f"CREATE TABLE IF NOT EXISTS {dn_len_table} (id text, {dn_col} text)")

# Copy rows from the dn_table to dn_len_table where the length of domain_name until the tld is equal to char_length
cursor.execute(f"""
    INSERT INTO {dn_len_table} (id, {dn_col})
    SELECT id, {dn_col}
    FROM {dn_table}
    WHERE LENGTH(SUBSTR({dn_col}, 1, INSTR({dn_col}, {tld}) - 1)) = {char_length}
""")


# Commit your changes and close the connection
db_connection.commit()
db_connection.close()