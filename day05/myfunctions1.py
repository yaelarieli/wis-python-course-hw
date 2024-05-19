def count_characters(text):
    line_conter = {'lines' : 0}
    word_counter = {'words' : 0}
    character_counter = {}
    
    for ch in text:
        if ch == "\n" or ch == " ": 
            continue
        if ch not in character_counter:
            character_counter[ch] = 1
        else:
            character_counter[ch] += 1
            
    line_conter['lines'] = text.count('\n') + 1
    word_counter['words'] = len(text.split())
            

    return word_counter, line_conter, character_counter


def display(word_counter, line_conter, character_counter):
    print(f"There are {len(character_counter)} characters in the file.")
    print(f"There are {line_conter['lines']} lines in the file.")
    print(f"There are {word_counter['words']} words in the file.")