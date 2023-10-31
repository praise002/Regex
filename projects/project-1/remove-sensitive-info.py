import re, pyperclip

# since we are not using search or find_all it will simply return the content whether or not it finds SSN

def remove_social_security_number():
    copied_text = pyperclip.paste()
    
    # replace with XXXXX...
    # replaced_text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', copied_text)
    # print(replaced_text)
    
    ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    replaced_text = re.sub(ssn_pattern, 'XXX-XX-XXXX', copied_text)
    pyperclip.copy(replaced_text)
    print('Copied to clipboard.')
    return replaced_text
    
def remove_credit_card_number():
    copied_text = pyperclip.paste()
    
    credit_card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    replaced_text = re.sub(credit_card_pattern, 'XXXX-XXXX-XXXX-XXXX', copied_text)
    pyperclip.copy(replaced_text)
    print('Copied to clipboard.')
    return replaced_text
    
if __name__ == '__main__':
    remove_social_security_number()
    remove_credit_card_number()