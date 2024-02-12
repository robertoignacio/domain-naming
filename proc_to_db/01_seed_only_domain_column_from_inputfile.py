# import sqlite3
# from tqdm import tqdm

# Description: This script reads a file line by line and inserts the data into a sqlite database table.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
tld_s = cv.tld_s

# Table and column names
dn_table = cv.dn_table
dn_col = cv.dn_col

tqdm = cv.tqdm

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# Create table
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {dn_table}
    ({dn_col} TEXT PRIMARY KEY)
''')

# read the file line by line
# input_file = open(f'../inputfiles/dummy.txt', 'r')
input_file = cv.input_file

# Insert data to the db table
with input_file as file:
    # Find the total row number to use in the progress bar
    lines = file.readlines()
    num_lines = len(lines)
    # Insert data, with progress bar
    for line in tqdm(lines, total=num_lines, desc="Seeding the db... "):
        # Split the line by the tab delimiter and take the first element
        value = line.strip().split('\t')[0].rstrip('.')
        # insert a row into the table only if the value does not already exist
        cursor.execute(f'''
            INSERT OR IGNORE INTO {dn_table} ({dn_col}) VALUES (?)
        ''', (value,))

# Because ICANN CDZ files contain duplicates (more than 1 dns for each domain name url), remove them
# Fetch all the rows in the table (may suffer from memory issues if the table is too large)
cursor.execute(f'SELECT DISTINCT * FROM {dn_table}')
distinct_rows = cursor.fetchall()

# Create a progress bar with the number of distinct rows as the total
progress_bar = tqdm(total=len(distinct_rows), desc="Off duplicates... ")

# Remove duplicate rows: create a new table without duplicates, delete the old table, rename the new table
# Create a new table: no duplicates
dn_table_no_duplicates = str('domain_names_table_no_duplicates')
assert dn_table_no_duplicates.isidentifier(), "null"

cursor.execute(f'''
    CREATE TABLE {dn_table_no_duplicates} AS
    SELECT DISTINCT * FROM {dn_table}
''')

# Update the (second) progress bar for each distinct row
for _ in distinct_rows:
    progress_bar.update()

# Close the (second) progress bar
progress_bar.close()

# Print a message before dropping the table
print("Cleaning...")

# Delete the old table
cursor.execute(f'''
    DROP TABLE {dn_table}
''')

# Rename the new table
cursor.execute(f'''
    ALTER TABLE {dn_table_no_duplicates} RENAME TO {dn_table}
''')

# Commit the changes
db_connection.commit()
db_connection.close()

print("Done :D")