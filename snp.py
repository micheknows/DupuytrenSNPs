# Here is the site for the API https://www.ncbi.nlm.nih.gov/research/snpdelscore/api/
# I am getting all SNPs(single nucleotide variants on Chromosome 14, since that Chromosome is suspected to be
# associated with Dupuytren's Disease

# The data only produces a 2KB file -- oh i realized why -- the next value
# It is still downloading, so I'll update the size once I figure it out

# Each result contains the following data
#   name    :   the name of the SNP (ex.  rs28973059)
#   pos     :   the position of the SNP on the chromosome
#   ref     :   the "normal" nucleotide
#   alt     :   the "variant" nucleotide
#   chr     :   the chromosome number (example format:  "chr14")
#   method  :   the method
#   tissue  :   tissue where found
#   value   :   ??

import requests
import json

filename = "json_data.json"

# get all SNPs from chromosome 14
query = '&chr=chr14'
base = 'https://www.ncbi.nlm.nih.gov/research/snpdelscore/api/snpdata/?chr=chr14&format=json'
url = base  + query

# send the request
r = requests.get(base)

# get the data
json_data = r.json()
print("Example of first page of data:  ")
for key, value in json_data.items():
    print(key + ":", value)

# parse out the results and start accumulating in my data file
json_results = json_data["results"]
while json_data["next"] != "None":
    # if the "next" value contains another API call, then keep going
    r = requests.get(json_data["next"])
    json_data = r.json()
    # add new results to the existing
    json_results.extend(json_data["results"])
    print("Next is " + json_data['next'])
    # I started saving as I went on purpose, instead of waiting until the end - it might make it slower, but...
    # For one thing, I could ensure it was working before going through the whole thing to check
    # Secondly, if something happened to stop it, I could see the number of entries for how far I had gotten and
    #    even the "next" api call and start from there
    with open(filename, 'w') as outfile:
        json.dump(json_results, outfile)
        print("Done and saved as " + filename)
        print("There are " + str(len(json_results)) + " entries.")


