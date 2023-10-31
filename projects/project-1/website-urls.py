import re, pyperclip

matches = []

def extract_website_urls():
    copied_text = pyperclip.paste()
    
    website_regex = re.compile(r'''(
        (https?://)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?
        )''', re.VERBOSE)
    
    for groups in website_regex.findall(copied_text):
        matches.append(groups[0])
        
if __name__ == '__main__':
    extract_website_urls()
    
    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard.')
        print('\n'.join(matches))
    else:
        print('No website urls found.')