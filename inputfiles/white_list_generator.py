import requests

# URL of the IANA mantained list of TLDs
url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"

# Send a HTTP request to the URL of the file
response = requests.get(url)

# Make sure the request was successful
response.raise_for_status()

# Get the Last-Modified header
white_list_last_modified = response.headers.get('Last-Modified')
print(f"Last-Modified: {white_list_last_modified}")

# Store the content of the response in a variable in-memory
content = response.text

# A list to store each (row) line from content as a list item
content_list = content.splitlines()

allowed_charset = '-0123456789abcdefghijklmnopqrstuvwxyz'

white_list = []

# Iterate over each item in content_list
for item in content_list:
    # Check if all characters in the item are in allowed_charset
    if all(char in allowed_charset for char in item.lower()):
        # If they are, add the item to white_list
        white_list.append(item.lower())

print(white_list)

# Create the file with write mode
with open('./iana_tld_white_list.txt', 'w') as f:
    # Write each item in the list to the file
    for item in white_list:
        f.write(f'{item}\n')