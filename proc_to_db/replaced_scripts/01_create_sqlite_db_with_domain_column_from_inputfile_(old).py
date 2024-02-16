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

# Add a new column 'id' to your table, id type is text
# SQLite does not support the IF NOT EXISTS clause when adding a column, trying...
try:
    cursor.execute(f'''
        ALTER TABLE {dn_table} ADD COLUMN id text
    ''')
except sqlite3.OperationalError as e:
    if 'duplicate column name' in str(e):
        pass  # Column already exists, do nothing
    else:
        raise  # re-raise the exception

# If you need to purge the ids, set the value of the 'id' column to NULL for all rows
cursor.execute(f"UPDATE {dn_table} SET id = NULL")

# Get the number of rows in the table
cursor.execute(f"SELECT COUNT(*) FROM {dn_table}")
rows_count = cursor.fetchone()[0]

# Populate the 'id' column with unique identifiers
# Fetch all rows into a list
rows = list(cursor.execute(f"SELECT rowid, * FROM {dn_table}"))

# Iterate over each row in the list
for row in tqdm(rows, desc="Populating the 'id' column... "):
    # Generate a unique ID
    unique_id = str(uuid.uuid4())
    
    # Assign the unique ID to the 'id' column of the current row
    cursor.execute(f"UPDATE {dn_table} SET id = ? WHERE rowid = ?", (unique_id, row[0]))

# Reorder the columns: from ['domain_name', 'id'] to ['id', 'domain_name']. Unsupported by SQLite.
# Why here? You cannot know the row number without first creating the domain_names_table table
# TBA: refactor at origin

# Create a new table with the desired column order
print("Reordering columns... ")
cursor.execute(f"CREATE TABLE IF NOT EXISTS colreorder_table (id text, {dn_col} text)")
# Copy the data from the old table to the new one
cursor.execute(f"INSERT INTO colreorder_table (id, {dn_col}) SELECT id, {dn_col} FROM {dn_table}")
# Delete the old table
cursor.execute(f"DROP TABLE {dn_table}")
# Rename the new table to the old table's name
cursor.execute(f"ALTER TABLE colreorder_table RENAME TO {dn_table}")

# Commit the changes
db_connection.commit()
db_connection.close()

print("Done :D")