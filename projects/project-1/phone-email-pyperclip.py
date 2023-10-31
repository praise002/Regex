import re, pyperclip

# get text off the clipboard
# Find all phone numbers and email addresses in the text.
# Paste them onto the clipboard.
# let us assume phone numbers follows this regex standard
# you can optionally save it to a file

matches = []

def extract_email():
    # get the text off the clipboard
    copied_text = pyperclip.paste()
    
    # create a regex for email addresses
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ # username
        @ # @ symbol
        [a-zA-Z0-9.-]+ # domain name
        (\.[a-zA-Z]{2,4}) # dot-something
        )''', re.VERBOSE)
    
    # find all matches in the clipboard text
    for groups in email_regex.findall(copied_text):
        matches.append(groups[0])
    
        
def extract_phone_number():
    # get the text off the clipboard
    copied_text = pyperclip.paste()
    
    # create a regex for phone numbers
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        (\s|-|\.)? # separator
        (\d{3}) # first 3 digits
        (\s|-|\.) # separator
        (\d{4}) # last 4 digits
        )''', re.VERBOSE)
    
    # find all matches in the clipboard text
    for groups in phone_regex.findall(copied_text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        matches.append(phone_num)

if __name__ == '__main__':
    extract_email()
    extract_phone_number()
    
    # Copy results to the clipboard if a match was found else execute the else statement
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard.')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')

    
    