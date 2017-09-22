# Check that it accepts a .txt file.
# Read the contents.
# Store the word.
# Top 10 frequently occouring words.
# If frequency is a odd number, square the number and show.

# Python <filename.py>(Argument 0 of the sys.argv function) <textfile.txt>(Argument 1 of the sys.argv function)

# Import statements
import sys
import os
import functools

# Check if there are two arguments
# 1) A python file
# 2) A text file
if len(sys.argv) != 2:
	print "Invalid arguments. Please use 'Python <filename.py> <textfile.txt>' "
	sys.exit()
	

# Check if file path is incorrect.
if(not(os.path.exists(sys.argv[1]))):
	print "Please check your file path. Put .py and .txt in the same folder or define the path explicitly"
	sys.exit()

# Check the extension. If the extension is not .txt, throw an error.
if sys.argv[1].split('.')[-1] != "txt":
	print "Invalid file format. Please use a text(.txt) file."
	sys.exit()

# Open the second argument that is passed(0-1st
escape = open(sys.argv[1])

# Define a dictionary
word_dic = {}

# Split the line by spaces to get the list of words
for line in escape:
    myline = line.split()
    for word in myline:
        w = word_dic.get(word,0)
        word_dic[word] = w + 1
    
# For each word in the list of words
# 
# 

    
print (word_dic, "\n")

search = raw_input("Enter the search string: ")

if search in word_dic:
    print "Found word %s %d times" %(search, word_dic[search])
else:
    print "Sorry. Not Found. "
    
# Display in descending and ascending order
print ("Original dictionary of words \n", word_dic.items())

sorted_list = []

# Sorted returns a list and not a dictionary
# Sorting in descending order
sorted_list = sorted(word_dic.items(), reverse=True)
print ("Sorting in descending order\n",sorted_list)

# Sorting in ascending order
sorted_list = sorted(word_dic.items())
print ("Sorting in ascending order", sorted_list)

# Sort by the value in dictionary is ascending and descending order
# Using the lambda function
sorted_list = sorted(word_dic.items(), key = lambda X: X[1])
print ("Sorting in ascending order of value occourence\n", sorted_list)

sorted_list = sorted(word_dic.items(), key = lambda Y: Y[1], reverse=True)
top_ten_words = sorted_list
print ("Sorting in descending order of value occourence\n", sorted_list)


top_ten = []
for i in range(10):
    try:
        word_tuple = sorted_list[i]
        top_ten.append(len(word_tuple[0]))
        print (word_tuple[0], ", Frequency: ", word_tuple[1], ", Length: ", len(word_tuple[0]))
    
    except IndexError:
        print ("The file has less than 10 words.\n")
        break
        
print ("Length of 10 most frequently occouring words: ")
print (top_ten)

print ("Top ten most frequently occouring words")
for i in range(10):
    print (top_ten_words[i])


mysum = functools.reduce(lambda x,y: x+y, top_ten)
print ("Average length of top ten words: ", mysum/len(top_ten))


squares = [x**2 for x in top_ten if x%2 != 0]
print ("Squares of odd word lengths: \n")
print (squares)
