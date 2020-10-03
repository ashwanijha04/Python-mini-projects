total = 13
nosp = 0
t = 1
print("GAME INTRUCTIONS")
print("This is a dual game. On the other side there will be computer.")
print("There will be total 13 sticks.Each player chooses min. 1 and max. 4 sticks in one turn. The player who has last stick will wins")


player1 = input("What is player 1's name?")
player2 = input("What is player 2's name?")


while total:
    print("Number of sticks remaining: ", total)
    print ("Player", t, "'s turn.")
    nosp = int(input("Pick minimum 1 and maximum 4 sticks.\n"))
    if nosp > total or nosp > 4 or nosp < 1:
	print("That is not allowed. Try picking again.")
        continue
    total -= nosp
    if t == 1:
        t = 2
    elif t == 2:
        t = 1

if t == 1:
    print (player2 + " won!!")
else:
    print (player1 + " won!!")