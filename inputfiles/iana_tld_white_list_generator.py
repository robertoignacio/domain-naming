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

white_list = []

# Split the content into lines, convert each line to lowercase, and add it to the list
for line in content.splitlines():
    # Check if the line starts with #
    if not line.startswith('#'):
        # If it doesn't, append it to the list, as strings in lowercase
        white_list.append(str(line.lower()))

# Create the file with write mode
with open('./iana_tld_white_list.txt', 'w') as f:
    # Write each item in the list to the file
    for item in white_list:
        f.write(f'{item}\n')
