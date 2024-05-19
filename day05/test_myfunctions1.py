from myfunctions1 import count_characters
import pytest



def test_count_characters():
    filename = "file1.txt"
    with open(filename) as fh:
        text = fh.read()
    word_result, line_result, character_result = count_characters(text)
    assert(word_result['words'] == 4)
    assert(line_result['lines'] == 2)
    assert(len(character_result) == 13)