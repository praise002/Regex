import re, pyperclip

# 3/14/2015, 03-14-2015, and 2015/3/14 - starts with month, day, year starts with year, month, day
# the single format will be DD-MM-YY

matches = []

def clean_up_dates():
    copied_text = pyperclip.paste()
    date_regex = re.compile(r'\d{1,2}[-/]\d{1,2}[-/]\d{4}|\d{4}[-/]\d{1,2}[-/]\d{1,2}')
    # print(date_regex.findall(copied_text))
    for groups in date_regex.findall(copied_text):
        if r'/' in groups:
            splitted_groups = groups.split(r'/')
        else:
            splitted_groups = groups.split('-')
        # split then substitute
        
        # print(splitted_groups)
        if len(splitted_groups[0]) == 4:
            # print(f'{splitted_groups[2]}-{splitted_groups[1]}-{splitted_groups[0]}')
            standard_format = '-'.join([splitted_groups[2], splitted_groups[1], splitted_groups[0]])
        else:  # use string formatting
            standard_format = f'{splitted_groups[1]}-{splitted_groups[0]}-{splitted_groups[2]}'
            
        # print(standard_format)
        matches.append(standard_format)  

def run():
    clean_up_dates()
    
    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard.')
        print('\n'.join(matches))
    else:
        print('No dates match found.')
        
if __name__ == '__main__':
    run()  