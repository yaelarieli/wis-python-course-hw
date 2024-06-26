from Bio import Entrez
Entrez.email = "yael.arieli@weizmann.ac.il"

termx = "Lion"

handle = Entrez.esearch(db="nucleotide", term=termx, idtype="acc", retmax=30)
record = Entrez.read(handle)
print(record["Count"])       # 538
print(record["IdList"])      # ['MK792700.1', 'MK792699.1', 'MK792698.1', ..., 'MK792681.1']
print(len(record["IdList"])) # 30
handle.close()


# term = "Orchid"
# 530077
# ['NZ_SELD00000000.2', 'NZ_SELD02000072.1',