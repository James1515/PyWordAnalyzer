#
# Author:  James Ortiz
# File:    wordAnalyzer.py
# Purpose: This program is designed to read in a file,
# create a list of lists, and then provide analytical
# information.
# Compile: python3 wordAnalyzer.py
#

# function lexicographicalSort(str)
# Python function to sort the words in lexicographical 
# order
# input: a valid string 'str' type
# returns: a lexicographically sorted list


def lexicographicalSort(myList): 
    # Split the myList till where space is found. 
    words = myList.split() 
    # sort() will sort the strings. 
    words.sort() 
    #return words of the string as a list:
    return words


# function wordCounter(str, list)
# Python function to count the instance
# of a single word in a list.
# Returns: an integer value

def wordCounter(strng, mylist):
    counter = 0
    for element in mylist:
        if strng == element:
            counter += 1

    return counter



# function map_writing(list)
# Python function to create 
# hash-map from a list.
# Returns: a hash-map (dictionary)
def map_book(mylist):

    #Declare empty hash-map:
    hash_map = {}

    if mylist is not None:
        for element in mylist:
            #Remove Punctuation:
            word = element.replace(",", "")
            word = word.replace(".", "")

            #Does the word exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1
    #Return hash_map, else Nothing
        return hash_map
    else:
        return None

            
    


def main():

    #Display Menu:
    print("Welcome to the Word Analyzer!")
    fileNameInput = input("Please enter an input(.txt) file: ")
    fileNameOutput = input("Please enter an output(.txt) file: ")
    stringValue = input("Enter a word you want to find the frequency of: ")


    
    #Open file
    file = open(fileNameInput, 'r')
    # Read from file, strip result, assinging to text
    text = file.read().strip()
    # Close file:
    file.close()

    #Bring letters down to lower-case:
    nString = ""
    nString = text.lower()

    #Sort list lexicographically, return list:
    nString = lexicographicalSort(nString)
    #print(nString)

    #Create Hash-Map from same list:
    HashMap = map_book(nString)
    
    numStrng = wordCounter(stringValue, nString)
    
    #Create a single string from the list:
    s = " "
    s = s.join(nString)


    freq = "Number of times the string: " + stringValue + " appears: " \
           + str(numStrng) + " time(s) \n"

    header = "####################################\n" \
             "#Author: James Ortiz  \n" \
             "#File:  " + fileNameOutput + " \n" \
             "####################################\n"

    lexi = "Output of " + fileNameInput + " in lexicographical (Dictionary order):\n"

    displayHeader = "Word/Words:       Frequency:\n"
    
    reverse = "Output in reverse order:\n"
    
    #Make the string output each character with new line
    #s = s.replace(' ', '\n')
    
    #Open/create new file called 'output.txt'
    outputFile = open(fileNameOutput, 'w')
    #Write information to file:
    outputFile.write(header)
    outputFile.write(freq)
    outputFile.write(lexi)
    outputFile.write(displayHeader)
    
    for key, value in HashMap.items():
        #print values at alignment:
        pValues = '{:>12}  {:>12}\n'.format(str(key), str(value))
        outputFile.write(pValues)  
    outputFile.close()  #close file
    print("Analysis Complete...")
    
if __name__ == "__main__":
    main()
