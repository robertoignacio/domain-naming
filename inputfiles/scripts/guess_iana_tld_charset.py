# Initialize an empty set to store the unique characters
# Set, because it will read the file as it comes and will not know which characters are first
unique_chars = set()

# Open the file and read its contents
with open('../white_list_iana_tlds_all.txt', 'r') as f:
    for line in f:
        # Add each character in the line to the set
        for char in line:
            # Check if the character is alphanumeric or a hyphen
            if char.isalnum() or char == '-':
                unique_chars.add(char)

# Convert the set to a list and sort it
unique_chars = sorted(list(unique_chars))

# Concatenate the items in the list into a string
unique_chars_str = ''.join(unique_chars)

# Export unique_chars_str to a file
with open('../iana_tld_charset.txt', 'w') as f:
    f.write(unique_chars_str)