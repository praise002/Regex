import re

def regex_strip(input_string, chars_to_remove=None):
    if chars_to_remove is None:
        # If chars_to_remove is not specified, remove leading and trailing whitespace
        pattern = r'^\s+|\s+$'
        
    else:
        # Escape characters that might be interpreted as regex metacharacters(.*?^$+)
        chars_to_remove = re.escape(chars_to_remove)
        # Create a pattern that matches characters specified in the second argument
        pattern = f'[{chars_to_remove}]+'  #['hello']+ 1 or more so it picks any matching pattern in the bracket

    
    return re.sub(pattern, '', input_string)
    
if __name__ == '__main__':
    input_string = input('Input a string: ')
    chars = input('Input a character to escape: ')
    
    # TEST
    # input_string = "ABCDEFHello, World!ABCDEF"
    # chars = "ABCDEF"
    
    # input_string = "   Hello, World!   "
    
    print(regex_strip(input_string, chars))