import argparse
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Define command line arguments
parser = argparse.ArgumentParser(description='List ASNs in a given country.')
parser.add_argument('country', type=str, help='the country code (ISO 3166-1 alpha-2) to list ASNs for')
parser.add_argument('-r', '--raw', action='store_true', help='print raw HTML data')
parser.add_argument('-t', '--text', action='store_true', help='print table in plain text')
parser.add_argument('-s', '--sort', action='store_true', help='sort table by number of IPs')
parser.add_argument('-e', '--export', action='store_true', help='export table to file in plain text')
args = parser.parse_args()

# Define URL and headers
url = f'https://ipinfo.io/countries/{args.country.upper()}'
headers = {'User-Agent': 'Mozilla/5.0'}

# Fetch webpage
response = requests.get(url, headers=headers)
html_data = response.text

# Parse HTML data
soup = BeautifulSoup(html_data, 'html.parser')

# Find IP address table
ipinfo_table = soup.find('table', {'class': 'table table-responsive'})
if not ipinfo_table:
    print(f"No data found for {args.country.upper()} on ipinfo.io")
    exit()

# Get table rows
ipinfo_rows = ipinfo_table.find_all('tr')[1:]

# Initialize table data
table_data = []

# Parse IP info data
for row in ipinfo_rows:
    asn, name, ips = [col.get_text().strip() for col in row.find_all('td')]
    table_data.append([asn, name, ips])

# Sort table by number of IPs (if --sort flag is set)
if args.sort:
    table_data.sort(key=lambda x: int(x[2]), reverse=True)

# Print raw HTML data (if --raw flag is set)
if args.raw:
    print(html_data)
    exit()

# Print table in plain text (if --text flag is set)
if args.text:
    print(tabulate(table_data, headers=['ASN', 'Name', 'Num IPs'], tablefmt='plain'))
    exit()

# Export table to file in plain text (if --export flag is set)
if args.export:
    with open(f"{args.country.upper()}_ASNs.txt", "w") as f:
        f.write(tabulate(table_data, headers=['ASN', 'Name', 'Num IPs'], tablefmt='plain'))
        print(f"Table exported to {args.country.upper()}_ASNs.txt")
    exit()

# Print table in a nice format
print(tabulate(table_data, headers=['ASN', 'Name', 'Num IPs']))
