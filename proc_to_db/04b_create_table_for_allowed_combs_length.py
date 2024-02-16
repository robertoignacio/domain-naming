import sqlite3
import itertools
from tqdm import tqdm # progress bar

import argparse # ArgumentParser(): Process an integer within a certain range.

# Description: This script will create a table for all combinations of allowed_characters at a specific length.
# For example, with char_length = 3, and allowed_characters = 'abcde', the table will have the following rows:
# abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde

# Input variables, from white list
# defined tld
tld = str(".dev")
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# Define the character length
char_length = int()

# Define the allowed char length range:
# (Beware of over 5: the db file enlarges significantly)
min_char_length_value = 1
max_char_length_value = 4

# Create the parser
parser = argparse.ArgumentParser()

# Add the integer argument
parser.add_argument('int_arg', type=int, help=f'An integer within the range {min_char_length_value} to {max_char_length_value}')

# Parse the arguments
args = parser.parse_args()

# ----------------------------------------------
# Allowed characters
allowed_characters = open('../inputfiles/iana_tld_charset.txt', 'r').read()

# ----------------------------------------------

def create_combinations_table(char_length):

    # sqlite db path
    db_path = f'../db_store/{tld_s}_tld_domain_names.db'
    # db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
    db_connection = sqlite3.connect(db_path)

    # Cursor, to execute SQL commands
    cursor = db_connection.cursor()

    # Create table for all combinations of characters at a specific length
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS all_comb_length_{char_length}
        (id_comb INTEGER, combination TEXT)
    ''')

    # ----------------------------------------------
    # Create all combinations of the allowed characters of the given length
    combinations = itertools.product(allowed_characters, repeat=char_length)

    total_combinations = len(allowed_characters) ** char_length

    # Insert each combination into the combinations_table
    for i, combination in tqdm(enumerate(combinations), total=total_combinations, desc='Inserting combinations... '):
        combination_str = ''.join(combination)
        cursor.execute(f'''
            INSERT INTO all_comb_length_{char_length} (id_comb, combination)
            VALUES (?, ?)
        ''', (i, combination_str))

    # Commit the changes and close the cursor
    db_connection.commit()
    cursor.close()
    db_connection.close()


# ----------------------------------------------
    
# Check if the argument is within the range
if min_char_length_value <= args.int_arg <= max_char_length_value:
    char_length = args.int_arg
    # Call the function:
    create_combinations_table(args.int_arg)
else:
    print(f'The argument is out of range: {args.int_arg}')
