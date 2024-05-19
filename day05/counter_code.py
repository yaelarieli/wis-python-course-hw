import sys
from myfunctions1 import count_characters,display

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()

    word_counter, line_conter, character_counter = count_characters(text)

    display(word_counter, line_conter, character_counter)

main()