def clean(file) -> list:
    file = open(file,'r') # open the file
    strlist = [word[:-1] for word in file.readlines()] # create a list with all lines in the string as elements excluding the last special newline character
    return list(set(strlist)) # convert list into set to remove non-unique repeats and convert back to list


def read(words: list, wordlen: str) -> list:
    numofWords = len(wordlen.split(" "))
    lenlist = [word for word in words if word.count(" ") == numofWords-1] # check for all elements in the supplied list for spaces, if spaces + 1 == number of words then add the element
    output = []
    counter = 0 # counter to check if all words in the element satisfy the wordlen condition

    for word in lenlist: # iterate through all elements of lenlist 
        counter = 0

        for i,x in enumerate(word.split(" ")): # split the word between each space and check if its length satisfies the condition
            if len(x) == len(wordlen.split(" ")[i]):
                counter += 1

        if counter == numofWords:
            output.append(word)

    return output



print(read(clean("words.txt"),"____ ____"))