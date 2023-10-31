import re, pyperclip

def remove_typos_in_word():
    copied_text = pyperclip.paste()
    
    # Define a regex pattern for multiple spaces between words
    multiple_spaces_pattern = re.compile(r'\s{2,}')
    # multiple_spaces_pattern = re.compile(r'(?<!\n)\s{2,}')
    replaced_text = re.sub(multiple_spaces_pattern, ' ', copied_text)
    # print(replaced_text)
    
    # Define a regex pattern for accidentally repeated words
    repeated_words_pattern = re.compile(r'(\b\w+\b)(\s+\1)+')
    replaced_text = re.sub(repeated_words_pattern, r'\1', replaced_text)
    # print(replaced_text)
    
    # Define a regex pattern for multiple exclamation marks at the end of sentences
    multiple_exclamations_pattern = re.compile(r'!{2,}')
    replaced_text = re.sub(multiple_exclamations_pattern, '!', replaced_text)
    # print(replaced_text)
    return replaced_text


if __name__ == '__main__':
    replaced_text = remove_typos_in_word()
    pyperclip.copy(replaced_text)
    print('Copied to clipboard.')
    print(replaced_text)
    