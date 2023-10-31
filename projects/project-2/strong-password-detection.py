import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # If all conditions are met, the password is strong
    return True
        
     
if __name__ == '__main__':
    password = input('Write your password: ')
    
    if is_strong_password(password):  # if True
        print('The password is strong.')
    else:
        print('The password is not strong.')