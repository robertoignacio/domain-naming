# import sqlite3

# Description: This script prints all the tables in a sqlite database file, column names, and the number of rows in each table

# Variables for the control flow of the program
# control_vars.py is at the same directory (level) as this file
import control_vars as cv


# Connect to the db
# db_connection = sqlite3.connect(cv.db_path)
db_connection = cv.db_connection
# Create a cursor
cursor = db_connection.cursor()

# ------------------------------
def print_tables(db_path): 
    # Get the list of all tables in the sqlite database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # Fetch all tables
    tables = cursor.fetchall()

    # For each table, get the row count and print it
    # To be alble to sort the table names, we need to store the table names and row counts in a list
    table_counts = []

    # Iterate over each table
    for table in tables:
        # Get the row count
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        # Index the tuple
        row_count = cursor.fetchone()[0]
        # Append to table_counts
        table_counts.append((table_name, row_count))

        # Get the column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        # Fetch all table columns
        columns = cursor.fetchall()
        # The column name is the second element in the tuple
        column_names = [column[1] for column in columns]
    
    # Sort the table name in descending order
    table_counts.sort(key=lambda x: x[0], reverse=False)

    # Print the table names and counts
    for table_name, row_count in table_counts:
        print(f"{table_name}, rows: {row_count}, column names: {column_names}")
    
    # Close the connection
    db_connection.close()


# Use the function
print_tables(cv.db_path)