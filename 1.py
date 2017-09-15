# Check that it accepts a .txt file.
# Read the contents.
# Store the word.
# Top 10 frequently occouring words.
# If frequency is a odd number, square the number and show.

# Python <filename.py>(Argument 0 of the sys.argv function) <textfile.txt>(Argument 1 of the sys.argv function)

# Import statements
import sys
import os

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


