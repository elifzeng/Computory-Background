#!/usr/bin/env python
import urllib.parse
import urllib.request
import argparse
 
# parse input
parser = argparse.ArgumentParser( description="Convert ac from uniprot to PDB" )
parser.add_argument("-i",type=str,required=True, help="Input list file" )
parser.add_argument("-o",type=str, required = False, default = "output.list",help="Output file")
args = parser.parse_args()
infile = args.i
outfile = args.o

# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# query str
uniprot_list = list()
uniprot_list = [ x.strip() for x in open(infile) ]
query_str = "\t".join(uniprot_list)

url = 'https://www.uniprot.org/uploadlists/'
params = {
'from': 'PDB_ID',
'to': 'ACC',
'format': 'tab',
'query': query_str
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()

with open(outfile,'w') as ofp:
    ofp.write(response.decode('utf-8'))

