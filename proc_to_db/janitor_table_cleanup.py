# import sqlite3
# from tqdm import tqdm

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
all_combinations = cv.all_combinations

# Before running this script, run 02_what_tables_exist_in_db_and_rows.py to know which table to clean up
# Change the table name to be cleaned up from the imported variables
# Manually change the table to be dropped
delete_table_contents = ""

# "" is allowed for SQL column names
# '' is allowed for SQL literals

# progress bar
tqdm = cv.tqdm

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Create a cursor object
cursor = db_connection.cursor()


# Execute SQL Delete statement: clean up all table rows
cursor.execute(f'''
    DELETE FROM {delete_table_contents}
''')

# ------------------------
# Progress bar
# Get the number of rows in the table
cursor.execute(f'SELECT COUNT(*) FROM {delete_table_contents}')
num_rows = cursor.fetchone()[0]
# Create a progress bar
progress_bar = tqdm(total=num_rows)
# Rows from
cursor.execute(f'SELECT * FROM {delete_table_contents}')
# Fetch all rows
rows = cursor.fetchall()
# Update the progress bar
for row in rows:
    print(row)
    progress_bar.update()
# Close the progress bar
progress_bar.close()

# ------------------------
# Commit changes and close the connection
db_connection.commit()
db_connection.close()