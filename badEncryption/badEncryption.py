def garbageEncryption(string: str,allowedLetters:str, key:str) -> str:
    encryptdict = dict(zip([i for i in allowedLetters], [i for i in key]))
    return ''.join([encryptdict[i] for i in string])



print(garbageEncryption("apple","abcdefghijklmnopqrstuvwxyz","1234567890qwertyuiopasdfgh"))