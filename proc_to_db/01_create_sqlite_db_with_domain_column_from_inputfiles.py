import sqlite3
from tqdm import tqdm # progress bar

import control_vars as cv # From control_vars.py file, values to be set by a Control Panel.

# Description: This script creates a sqlite database file from a file that contains DNS records
# with this shape tab separated: domain name, TTL, DNS class, type of DNS Record, Name Server.

tld = cv.tld
# tld_s is for naming the files and tables
tld_s = str(tld.lstrip('.'))

# DNS records input file
#input_file = open(f'../inputfiles/icann_tld_{tld_s}_registered_domains_latest.txt', 'r')
input_file = open(f'../inputfiles/icann_tld_{tld_s}_registered_domains_dummy.txt', 'r')

# Create or connect to sqlite file db
# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)

# Cursor, to execute SQL commands
cursor = db_connection.cursor()

# ---------------------------------
# https://www.sqlite.org/lang_createtable.html
# Create table with two columns, with rowid (hidden column)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS main_domain_names_table
    (id INTEGER PRIMARY KEY, domain_name TEXT UNIQUE)
''')

# Note: Prisma ORM will not be able to recognize or map the id column (yet), 
# when the id column is type TEXT, like with uuid
# but will instrospect the columns correctly as fields.
# After instrospect, you have to manually define the id field in the schema.prisma file
# https://github.com/prisma/prisma/issues/16311

# [      domain_names_table      ]
# [ rowid ] [ id ] [ domain_name ]

# Read the input file and insert the data into the table
with input_file as file:
    # Find the total row number to use in the progress bar
    rows = file.readlines()
    num_rows = len(rows)
    # Read the file line by line (from top to bottom, left to right, one line at a time)
    # with progress bar
    # Insert insert a NULL value into the id column 
    # and the domain_name_value into the domain_name column for each line in the db
    for line in tqdm(rows, total=num_rows, desc="Seeding the db... "):

        # the id column is an INTEGER PRIMARY KEY, 
        # so SQLite will automatically generate a unique integer for this column when you insert NULL

        # Split the line by the tab delimiter and take the first element for the domain_name column
        domain_name_value = line.strip().split('\t')[0].rstrip('.')
        
        # Insert the data into the table only if the value does not already exist
        cursor.execute(f'''
            INSERT OR IGNORE INTO main_domain_names_table (id, domain_name)
            VALUES (NULL, ?)
        ''', (domain_name_value,))

# Because ICANN CDZ files contain duplicates (more than 1 dns for each domain name url), 
# the UNIQUE constraint will not allow the insertion of duplicate domain names,
# but the db file passed all the rows from the input file, so we have to remove the empty space
        
# Commit the insert operations
db_connection.commit()

print("Recovering unused db file space... ")
# Recover unused db file space
cursor.execute('VACUUM')

# Close the db connection
cursor.close()
db_connection.close()

print("Done :D")