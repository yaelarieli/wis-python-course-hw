from Bio import Entrez
from Bio import Entrez, SeqIO
import csv
from datetime import datetime
import pandas as pd

Entrez.email = "yael.arieli@weizmann.ac.il"


def search_ncbi(termx,numberx):
    
    handle = Entrez.esearch(db="nucleotide", term=termx, idtype="acc", retmax=numberx)
    record = Entrez.read(handle)
    Idlist1 = record["IdList"]
    total = record["Count"]
    handle.close()
    
    return(Idlist1,total)


def fetch_ncbi(doc_id,filename):

    handle = Entrez.efetch(db="nucleotide", id=doc_id, rettype="gb", retmode="text")
    data = handle.read()
    handle.close()

    with open(filename, 'w') as fh:
        fh.write(data)


    


def new_items_csv(filename,termx,numberx,total):
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_entry = pd.DataFrame([[current_date_time, termx, numberx, total]],columns=['date', 'term', 'max', 'total'])
    
    try:
        # Try to append to the existing CSV file
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        updated_data = new_entry
    
    updated_data.to_csv(filename, index=False)

