# Sequence Analysis Program
This Python program analyzes DNA sequences in FASTA format and provides two main functionalities:

## 1. Most Common Character

* Finds the most frequently occurring character in the given sequence.
* Reports the character and the number of times it appears.


## 2. Longest Repeating Subsequence

* Identifies the longest sub-sequence that repeats itself within the input sequence.
* Reports the repeating subsequence and its length.

# Usage
The program is executed from the command line using the following syntax:
```
python hw9.py INPUT_FILE [OPTIONS]
```
Replace INPUT_FILE with the path to your FASTA file containing the sequence to be analyzed.

### Options

`--letter` or `-l`: Use this option to find the most common character in the sequence.
`--duplicate` or `-d`: Use this option to find the longest repeating subsequence.

You can specify one or both options depending on your analysis requirements.

The main program contained in the `hw9.py` file, while the required functions are defined in `func_for_hw9.py`.



