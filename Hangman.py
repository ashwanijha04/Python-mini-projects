import random
from words import word_list
from images import IMAGES

def get_word():
  word = random.choice(word_list)
  return word.upper()

def play(word):
  complete_word="_"*len(word)
  gussed_letters=[]
  gussed=False
  tries=8
  print("\t \t  Let's play hangman game ")
  print("\t",IMAGES[tries])
  while not gussed and tries >0:
    guess = input("\t Please Enter any letter and guess the word \n \t").upper()
    if len(guess)==1 and guess.isalpha():
      if guess in gussed_letters:
        print("YOU ALREADY GUESSED THE WORD  ")
        print(complete_word)
        print(IMAGES[8-tries])
        tries-=1
      elif guess not in word:
        print("OPPS!! guess not in words   ")
        print(IMAGES[8-tries])
        print(complete_word)
        tries-=1
        gussed_letters.append(guess)
        
      else:
        print("GOOD JOB "+guess+" IN WORDS")
        word_com_list=list(complete_word)
        for i in range(len(word)):
          if guess in word[i]:
            word_com_list[i]=guess
        complete_word="".join(word_com_list)
        print("The word so far guessed is :",complete_word)
        if "_" not in complete_word:
          gussed=True
        gussed_letters.append(guess)  
    else:
      print('NOT A VALID INPUT ')
  if gussed:
    print("CONGRATS,YOU WON THE GAME")
  else:
    print("SORRY YOU ARE RAN OUT OF TRIES THE WORD WAS -> "+word)


def main():
  var=get_word()
  play(var)
  while input("\t \t DO YOU WANT TO PLAY AGAIN ??? (Y/N)").upper=="Y":
    var=get_word()
    play(var)

main()