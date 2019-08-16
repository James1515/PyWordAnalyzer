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

#Used for characters in string:
#def frequencyCount(string, myList):
#    counter = 0
#    nstring = string
#    for i in myList:
#        if i == nstring:
#            counter = counter + 1
#    return counter


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
        
    
    

def main():

    #Taking in input to find the number of instances
    #in a string:
    stringValue = input("Enter a string: ")

    


    
    #Open file
    file = open('episodeIVCrawl.txt', 'r')
    # Read from file, strip result, assinging to text
    text = file.read().strip()
    # Close file:
    file.close()

    nString = ""
    nString = text.lower()

    #print(nString)
    
    #Find the frequency of a single character in the string here:
    
    #num = frequencyCount('a', nString)
    #print(num)

    
    nString = lexicographicalSort(nString)
    #print(nString)

    numStrng = wordCounter(stringValue, nString)
    #print(numStrng)
    #Create a single string from the list:
    s = " "
    s = s.join(nString)


    freq = "Number of times the string: " + stringValue + " appears: " \
           + str(numStrng) + "\n"

    header = "####################################\n" \
             "#Author: James Ortiz\n" \
             "#File:   output.txt \n" \
             "####################################\n"

    lexi = "Output in lexicographical (Dictionary order):\n"

    reverse = "Output in reverse order:\n"
    
    #Make the string output each character with new line
    s = s.replace(' ', '\n')
    
    #Open/create new file called 'output.txt'
    outputFile = open('output.txt', 'w')
    outputFile.write(header)
    outputFile.write(freq)
    outputFile.write(lexi)
    outputFile.write(s) #write to file
    outputFile.close()  #close file
    print("Analysis Complete...")
    
if __name__ == "__main__":
    main()
