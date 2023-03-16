# ASN List for a Country

This Python script fetches the list of ASNs for a given country from ipinfo.io.

### Requirements

make sure you have the required pachages by running

`pip install -r requirements.txt`

### Usage

`python fetch-asn-list.py [OPTIONS] COUNTRY_CODE`

#### Required Arguments

- `COUNTRY_CODE`: The 2-letter code for the country whose ASN list you want to generate. 

#### Optional Arguments

- `-r`, `--raw`: Export the raw HTML data to a file instead of parsing it.

- `-t`, `--table`: Export the ASN list to a text file in a table format.

- `-s, `--sort`: sort table by number of IPs.

- `e`, `--export`: export table to file in plain text.

#### Example Usage

`python fetch-asn-list.py ir`
