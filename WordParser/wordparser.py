
def removeRepeatedWordsFromFile(file) -> list:
    file = open(file,'r')
    strlist = [word[:-1] for word in file.readlines()] # create a list with all lines in the string as elements excluding the last special newline character
    return list(set(strlist)) # convert list into set to remove repeated strings and convert back to list

# takes list of strings and a string (like "___ ___") with matching number of words and length and searches for all strings that match 
def findStrings(words: list, conditionString: str) -> list: 
    numofWords = len(conditionString.split(" "))
    lenlist = [word for word in words if word.count(" ") == numofWords-1] # check for all elements in the supplied list that match the number of words in the supplied string
    output = []
    counter = 0 # counter to check if all words in the element satisfy the wordlen condition

    for word in lenlist: # iterate through all elements of lenlist 
        counter = 0

        for i,x in enumerate(word.split(" ")): # split the word between each space and check if its length satisfies the condition
            if len(x) == len(conditionString.split(" ")[i]):
                counter += 1

        if counter == numofWords:
            output.append(word)

    return output



#example: findStrings(removeRepeatedWordsFromFile("words.txt"),"___ __") returns all strings with 2 words of length 3 and 2 respectively