#!/usr/bin/python
import sys,os

if len(sys.argv)<2:
    print "Usage : $0 list_file"
    exit()
listfile=sys.argv[1]

database_path = '/data/SSD/PDB'
for line in open(listfile,"r"):
    pdbid=line.strip()
    if line:
        middle = pdbid[1:3]
        if not os.path.isfile("%s/%s/pdb%s.ent.gz"%(database_path,middle.lower(),pdbid.lower())):
            os.system("wget http://www.rcsb.org/pdb/files/%s.pdb.gz "%pdbid)
            os.system("gunzip -f %s.pdb.gz"%pdbid)
        else:
            print ">>>>> Get PDB file from local database: %s"%database_path 
            print ">>>>> PDB id %s"%pdbid
            os.system("cp %s/%s/pdb%s.ent.gz ./"%(database_path,middle.lower(),pdbid.lower()) )
            os.system("gunzip -f pdb%s.ent.gz"%pdbid.lower())
            os.system("mv pdb%s.ent %s.pdb"%(pdbid.lower(),pdbid.lower()))
            print ">>>>> Done" 
        
print "Done"

