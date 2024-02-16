# import sqlite3
import itertools

# Description: This script creates a table for all combinations of characters at a specific length.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

tld = cv.tld
char_length = cv.char_length
tqdm = cv.tqdm

all_combinations = cv.all_combinations

# Allowed characters
allowed_characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

# Create and/or connect to sqlite file db
db_connection = cv.db_connection

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# Create table for all combinations of characters at a specific length
# Table header: combination
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {all_combinations} ( 
        combination TEXT
    )
''')

# Generate all the combinations of the allowed_characters for char_length
combinations = [''.join(combination) + tld for combination in itertools.product(allowed_characters, repeat=char_length)]

# Insert the combinations into the table
for combination in tqdm(combinations, desc='Inserting combinations'):
    cursor.execute(f'INSERT INTO {all_combinations} VALUES (?)', (combination,))

# Commit the changes
db_connection.commit()

# Close the connection
db_connection.close()