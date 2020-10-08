import os
import urllib.request
import urllib.parse

def read_text():
	quotes = open(os.path.expanduser("movie_quotes.txt"))
	contents_of_file = quotes.read()
	print (contents_of_file + "\n")
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(text_to_check, safe=''))
	output = connection.read()
	connection.close
	if "true" in str(output):
		print ("Profanity Alert!")
	else:
		print ("Profanity free text!")

read_text()
