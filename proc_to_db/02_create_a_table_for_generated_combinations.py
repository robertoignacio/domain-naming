import sqlite3
import itertools
from tqdm import tqdm # progress bar

import argparse # ArgumentParser(): Process an integer within a certain range.

import control_vars as cv # From control_vars.py file, values to be set by a Control Panel.

# Description: This script will create a table for all combinations of allowed_characters at a specific length.
# For example, with char_length = 3, and allowed_characters = 'abcde', the table will have the following rows:
# aaa, bbb, ccc, abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde
# Without appending any tld. Instead of aaa.dev, its just aaa.

# Run as:
# python3 02_create_table_for_allowed_combs_length.py <int argument>
# <int argument> is the character length of the combinations to be created.
# Example: 
# python3 02_create_table_for_allowed_combs_length.py 3
# Better than manually changing the char_length value in the script.

# ----------------------------------------------
# Input variables, from a tld white list
# defined tld
tld = cv.tld
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# Initialize the character length variable
char_length = int()

# Define the allowed char length range:
# (Beware of over 5: the db file enlarges significantly)
min_char_length_value = 2
max_char_length_value = 4 # (over 4 is computationally expensive, beware)

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

# Criteria: Domain names cannot start or end with a hyphen or double hyphens, but they can start with 'xn--'
# Filter out combinations with that

def generate_filtered_combinations(char_length, allowed_characters):
    # Generate all possible combinations
    combinations = itertools.product(allowed_characters, repeat=char_length)

    # Convert the combinations to strings and filter out invalid names
    filtered_combinations = [''.join(combination) for combination in combinations 
                             if not (combination[0] == '-' or combination[-1] == '-' or '--' in ''.join(combination))]

    return filtered_combinations

# ----------------------------------------------

def create_combinations_table(char_length):

    # sqlite db path
    db_path = f'../db_store/{tld_s}_tld_domain_names.db'
    # db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
    db_connection = sqlite3.connect(db_path)

    # Cursor, to execute SQL commands
    cursor = db_connection.cursor()

    # Create a table for all combinations of characters at a specific length
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS all_combs_length_{char_length}
        (id_comb INTEGER, combination TEXT)
    ''')

    # ----------------------------------------------
    # Create all combinations of the allowed characters of the given length.
    filtered_combinations = generate_filtered_combinations(char_length, allowed_characters)

    # Get the length of the filtered_combinations
    combination_length = len(filtered_combinations)

    # Insert each filtered_combination into the combinations table.
    # enumerate(filtered_combinations) generates an index i for each combination in filtered_combinations
    for i, combination in tqdm(enumerate(filtered_combinations), total=combination_length, desc=f'Creating combinations table for length {char_length}'):

        cursor.execute(f'''
            INSERT INTO all_combs_length_{char_length} (id_comb, combination)
            VALUES (?, ?)
        ''', (i, combination))

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