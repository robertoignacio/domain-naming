import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get('https://www.iana.org/domains/root/db')

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the 'tld-table' in the parsed HTML
tld_table = soup.find('table', id='tld-table')

# Find the 'tbody' in the 'tld-table'
tbody = tld_table.find('tbody')

# Find all tr elements within the tbody
tr = tbody.find_all('tr')

'''
This shape: one row or <tr> element, containing three <td> elements

<tr>
  <td><span class="domain tld"><a href="">abc</a></span></td>
  <td>generic</td>
  <td>AAA</td>
</tr>
'''

# Write the output
with open('roots_tld_by_manager.tsv', 'w') as f:
    # Iterate over each row
    for row in tr:
        # Find all td elements within the row
        tds = row.find_all('td')
        
        # Extract the text from the first td, stripping the unwanted parts
        # The text by bs4 is "not inside < >"
        first_td_text = tds[0].find('a').text
        
        # Extract the text from the second and third tds
        second_td_text = tds[1].text
        third_td_text = tds[2].text
        
        # Write the extracted text to the file
        f.write(f'{first_td_text}\t{second_td_text}\t{third_td_text}\n')



