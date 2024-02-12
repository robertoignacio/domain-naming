# import sqlite3

# Description: This script prints the names of all the tables in a sqlite database file.

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv

# Connect to the db
db_connection = cv.db_connection
# Create a cursor
cursor = db_connection.cursor()

# ------------------------------
def print_table_names_and_row_counts(db_path): 
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # Fetch all tables
    tables = cursor.fetchall()

    # For each table, get the row count and print it
    # (a list, to keep the order of the tables)
    table_counts = []
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        # index the tuple
        count = cursor.fetchone()[0]
        # append
        table_counts.append((table_name, count))
    
    # Sort the table name in descending order
    table_counts.sort(key=lambda x: x[0], reverse=False)

    # Print the table names and counts
    for table_name, count in table_counts:
        print(f"{table_name}, rows: {count}")
    
    # Close the connection
    db_connection.close()


# Use the function
print_table_names_and_row_counts(cv.db_path)