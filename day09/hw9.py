import argparse
from func_for_hw9 import process_file, get_longest_seq,most_frequent_letter


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file name')
    parser.add_argument('--duplicate','-d', action='store_true')
    parser.add_argument('--letter','-l', action='store_true')
    args = parser.parse_args()
    filename = args.filename
    dna = process_file(filename, 'fasta')

    if not args.duplicate and not args.letter:
        parser.error('No action requested, add --duplicate or --letter')   


    if args.duplicate:
    
        longes_seq, length = get_longest_seq(dna)
        print(f'The longest sequence is: {longes_seq} and its length is: {length}')

    if args.letter:
        most_common_letter, most_common_count = most_frequent_letter(dna)
        print(f'The most common letter is: {most_common_letter} and its count is: {most_common_count}')

main()
