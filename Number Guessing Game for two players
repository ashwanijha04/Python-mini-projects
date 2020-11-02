choice = input('How many players? (1 or 2): ')
if choice in ('1'):
        player1 = str(input("\nEnter Your Name: "))
        if choice == '1':
           print('Welcome', '' ,player1.title())
        import random

        number = random.randint(1,6)

        attempts = 0
        guess = 0


        while guess != number:
         try:
            guess = eval(str(input('Guess number between 1 to 6:')))
         except NameError:
                 print('enter only numbers')
                 continue
         except SyntaxError:
                 print('no special characters allowed')
                 continue
         if guess not in range (1,7):
              print('enter only numbers between 1 to 6')
              continue


         attempts += 1

         if guess == number:
                 print (f'Correct! You used {attempts} attempts!')
                 break

         if guess < number:
                  print ('Go higher!')
         if guess > number:
                   print ('Go lower!')

if choice in ('2'):
       player2=str(input('\nEnter First Player Name: '))
       print(f'Welcome {player2.title()}!')
       player3=str(input('\nEnter Second Player Name: '))
       print(f'Welcome {player3.title()}!')
       import random

       number = random.randint(1,6)

       attempts1 = 0
       guess = 0
       print(f"\n{player2.title()} will play first.")
       while guess != number:
         try:
            guess = eval(str(input('\nGuess number between 1 to 6: ')))
         except NameError:
                 print('\tenter only number')
                 continue
         except SyntaxError:
                 print('\tno special characters allowed')
                 continue
         if guess not in range (1,7):
              print('\nenter only numbers between 1 to 6')
              continue


         attempts1 += 1


         if guess < number:
                  print ('Go higher!\n')
         if guess > number:
                   print ('Go lower!\n')

         if guess == number:
                 print (f'\nCorrect! You used {attempts1} attempts!')



                 print(f'\nNow {player3.title()} will play.')
                 import random

                 number = random.randint(1,6)

                 attempts2 = 0
                 guess = 0




                 while guess != number:
                  try:
                    guess = eval(str(input('\nGuess number between 1 to 6:')))
                  except NameError:
                         print('enter only number')
                         continue
                  except SyntaxError:
                         print('no special characters allowed')
                         continue
                  if guess not in range (1,7):
                      print('enter only numbers between 1 to 6')
                      continue


                  attempts2 += 1

                  if guess == number:
                         print (f'Correct! You used {attempts2} attempts!')
                         break


                  if guess < number:
                          print ('Go higher!\n')
                  if guess > number:
                           print ('Go lower!\n')





                 print('\nNow it is result time!')
                 if attempts1 < attempts2:
                  print(f'\n{player2.title()} HAS WON!')
                 elif attempts1 == attempts2 :
                  print('\nIt is a tie')
                 else:
                  print(f'{player3.title()} HAS WON!')
