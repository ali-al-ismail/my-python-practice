import string
import random

def generatePassword(len):
    output = []
    badCheckSym = 0
    badCheckLow = 0
    badCheckUpp = 0

    for i in range(len):
        letter = random.choice(string.ascii_letters + string.punctuation)
        output.append(letter)
    
    random.shuffle(output)
    return ''.join(output)




def managePasswords(file: str,site: str, username: str, passwordlength: int):
    f = open(file, 'a')
    f.write(f'Site: {site}   Username: {username}    Password: {generatePassword(passwordlength)}\n')
    f.close()



managePasswords(r"C:\Users\atarashi\Documents\Projects\Python\WordParser\k.txt","Youtube.com", "Ali", 5)


