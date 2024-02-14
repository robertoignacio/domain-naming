import requests

# The Public Suffix List is subject to the terms of the Mozilla Public // License, v. 2.0 https://mozilla.org/MPL/2.0/
url = 'https://publicsuffix.org/list/public_suffix_list.dat'

# Send a Get request to the URL:
response = requests.get(url)

# Store the content of the response as text in a (in-memory) variable:
content = response.text

# Split the content into lines
lines = content.splitlines()

# Initialize an empty list to hold the tuples
tuples_list = []

# Initialize an empty list to hold the lines of the current tuple
current_tuple_lines = []

# Iterate over the lines
for line in lines:
    # If the line is a newline character alone, end the current tuple and start a new one
    if line == '':
        # Add the current tuple to the list of tuples
        tuples_list.append(tuple(current_tuple_lines))
        # Start a new tuple
        current_tuple_lines = []
    # If the line does not contain "Removed" or "Bug", add it to the current tuple
    elif 'Removed' not in line and 'Bug' not in line:
        current_tuple_lines.append(line)

# Add the last tuple to the list of tuples if it's not empty
if current_tuple_lines:
    tuples_list.append(tuple(current_tuple_lines))

# Open the output file in write mode
with open('output.txt', 'w') as f:
    # Iterate over each tuple in the list
    for t in tuples_list:
        # Convert the tuple to a string and write it to the file
        f.write(str(t) + '\n')

# print the tuple number
print(len(tuples_list))
