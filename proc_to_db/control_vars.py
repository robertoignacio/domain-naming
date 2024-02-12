import sqlite3 # file db
from tqdm import tqdm # progress bar (not accessed here but where this file is imported)

# Variables for the control flow of the program
# Values that change often

# Table and column names
dn_table = str('domain_names_table')
dn_col = str('domain_name')

tld = '.dev'
tld_s = str(tld.lstrip('.'))
# These will be fed externally, TBA

# Table and column names
dn_table = str('domain_names_table')
dn_col = str('domain_name')

# SQL parametrization intent
# Ensure tld_s values are safe to include in the SQL command
assert tld_s.isidentifier(), "null"
assert dn_col.isidentifier(), "null"
assert dn_table.isidentifier(), "null"

# Define the character length (Beware of over 5, the db file enlarges significantly)
char_length = int(2)

# Table name for the domain names with a specific character length
dn_len_table = f'domain_names_length_{char_length}'
all_combinations = f'all_combs_length_{char_length}'

# Input file path
input_file = open(f'../inputfiles/icann_tld_{tld_s}_global_list_2024_02.txt', 'r')

# sqlite db path
db_path = f'../db_store/{tld_s}_tld_domain_names.db'
# db_connection = sqlite3.connect(f'../db_store/{tld_s}_tld_domain_names.db')
db_connection = sqlite3.connect(db_path)