import requests
dbs = 'pubmed'
querys = 'Dupuytren+Contracture[mesh]+AND+Polymorphism,+Single+Nucleotide[mesh]'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
url = base  + 'esearch.fcgi?db=' + dbs + '&term=' + querys + '&usehistory=y&retmode=json'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ":", value)

web = json_data['esearchresult']['webenv']
mykey = json_data['esearchresult']['querykey']
url = base + "esummary.fcgi?db=" + dbs + "&query_key=" + mykey + "&WEbEnv=" + web + "&retmode=json"
docsums = requests.get(url)
json_data = docsums.json()
for key, value in json_data.items():
    print(key + ":", value)
