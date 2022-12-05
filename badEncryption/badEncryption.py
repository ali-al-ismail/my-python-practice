
#poor way of encrypting a string by using a key for each letter
def garbageEncryption(string: str,alphabet:str, key:str) -> str:
    encryptdict = dict(zip([i for i in alphabet], [i for i in key])) # create a dictionary with the alphabet as the key and the key as the value
    return ''.join([encryptdict[i] for i in string])



#example: print(garbageEncryption("apple","abcdefghijklmnopqrstuvwxyz","1234567890qwertyuiopasdfgh"))