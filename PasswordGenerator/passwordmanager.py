import string
import random


# there is probably a better way to do this
def generatePassword(len: int) -> str:
    output = []
    for i in range(len):
        letter = random.choice(string.ascii_letters + string.punctuation) # random chooses from all english ascii letters and punctuation marks
        output.append(letter) 
    
    random.shuffle(output) # shuffle randomly for no reason
    return ''.join(output) # convert to string and return result



# takes file path, site name, user name, and password length for the generate password function
def managePasswords(file: str,site: str, username: str, passwordlength: int):
    f = open(file, 'a') # open in append mode
    f.write(f'Site: {site}   Username: {username}    Password: {generatePassword(passwordlength)}\n')
    f.close()



# example usage: managePasswords("passwords.txt","Youtube.com", "Ali", 10) 


