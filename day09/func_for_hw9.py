from Bio import SeqIO
import re
from collections import Counter


def process_file(filename, file_type):
    for seq_record in SeqIO.parse(filename, file_type):
        # print(seq_record.seq)
        dna = seq_record.seq
        dna = str(dna)
    return dna


def get_longest_seq(dna):
    
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        #print(regex)
        m = re.search(regex, dna)
        if m:
            result = m.group(1)
            length += 1
        else:
            break

    return result, len(result)

def most_frequent_letter(dna):
    # Use regular expression to find all letters in the sequence
    letters = re.findall(r'[ATCG]', dna.upper())

    letter_counts = Counter(letters)

    # Find the most common letter and its count
    most_common_letter, most_common_count = letter_counts.most_common(1)[0]

    return most_common_letter, most_common_count



