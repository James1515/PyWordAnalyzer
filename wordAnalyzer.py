#
# Author:  James Ortiz
# File:    wordAnalyzer.py
# Purpose: This program is designed to read in a file,
# create a list of lists, and then provide analytical
# information 
#

# function lexicographicalSort(str)
# Python function to sort the words in lexicographical 
# order   
def lexicographicalSort(my_string): 
    # Split the my_string till where space is found. 
    words = my_string.split() 
    # sort() will sort the strings. 
    words.sort() 
    # Iterate i through 'words' to print the words 
    # in alphabetical manner. 
    #for i in words: 
    #    print(i)
    return words


def main():
    file = open('episodeIVCrawl.txt', 'r')
    text = file.read().strip()
    file.close()

    newString = lexicographicalSort(text)

    s = " "
    s = s.join(newString)
    s = s.replace(' ', '\n')
    
    
    newFile = open('output.txt', 'w')
    newFile.write(s)
    
if __name__ == "__main__":
    main()
