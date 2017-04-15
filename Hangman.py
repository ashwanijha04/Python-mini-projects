#constants
import random
#Creating a tuple
HANGMAN = (
"""
    -----
    |    |
    |
    |
    |
    |
    |
-----------
""",

"""
    -----
    |    |
    |   o o
    |
    |
    |
    |
-----------
""",


"""
    -----
    |    |
    |   o o
    |  --+--
    |
    |
    |
-----------
""",


"""
    -----
    |    |
    |    o
    | /--+--
    |
    |
    |
-----------
""",

"""
    -----
    |    |
    |    o
    | /--+--/
    |    
    |    
    |
-----------
""",


"""
    -----
    |    |
    |    o
    | /--+--/
    |    |
    |    |
    |
-----------
""",

"""
    -----
    |    |
    |    o
    | /--+--/
    |    |
    |   ||
    |   |
-----------
""",


"""
    -----
    |    |
    |    o
    | /--+--/
    |    |
    |   |||
    |   | |
-----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("SCURRILOUS", "LIBEL", "VACCILATE", "EXTENUATE", "DESULTORY", "PREVARICATE"
         "ASPERSION", "STOLID", "BLASE", "ENTAIL")

word = random.choice(WORDS) #The word to be guessed
so_far = "-" * len(word)
wrong = 0
used = [] #list of letters already guessed


print "Welcome to hangman! Good luck"

while wrong < MAX_WRONG and so_far != word:
    print HANGMAN[wrong]
    print "You've used the following letters: \n", used
    print "The word so far guessed is : ", so_far

    guess = raw_input("Enter your guess: ")
    guess = guess.upper()
    used.append(guess)



    #Checking the guess
    if guess in word:
        print "\nYes! ", guess, " is in the word!"
        #create a new so_far to append guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print"\nSorry! The ", guess, " isn't in the word."
        wrong += 1

if wrong == MAX_WRONG:
    print HANGMAN[wrong]
    print "You know nothing Jon Snow!"

else:
    print "Lord Tyrion, you know everything!"
    print "The word was ", word, "and it's meaning is 'still to come'"


raw_input("Press enter to exit")
