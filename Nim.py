totalSticks = 13
numberOfSticksPicked = 0
turn = 1
print(
"""
This is a 2 player game.
The computer-human based game will be made soon.
There are a total of 13 sticks.
Each player choses minimum 1 and maximum 4 sticks in one turn.
The player who picks up the last stick wins.
All the best to both players.

""")

player1 = input("What is player 1's name?")
player2 = input("What is player 2's name?")

while totalSticks:
    print("Number of sticks remaining: ", totalSticks)
    print ("Player", turn, "'s turn.")
    numberOfSticksPicked = int(input("Pick minimum 1 and maximum 4 sticks.\n"))
    if numberOfSticksPicked > totalSticks\
    or numberOfSticksPicked > 4\
    or numberOfSticksPicked < 1:
        print("That is not allowed. Try picking again.")
        continue
    totalSticks = totalSticks - numberOfSticksPicked
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

if turn == 1:
    print (player2 + " won.")
else:
    print (player1 + " won.")
