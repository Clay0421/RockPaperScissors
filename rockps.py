#player1 = 'scissors'
#player2 = 'rock'

#the game
def the_game(player1, player2):
    if player1 == player2:
        print("It's a tie!")
        
    elif player2 == 'rock' or player2 == 'r':
        if player1 == 'scissors' or player1 == 's':
            print('Player 2 won!')
        else:
            print('Player 1 won!')
            
    elif player2 == 'paper' or player2 == 'p':
        if player1 == "scissors" or player1 == 's':
          print("Player 1 won!")

        elif player1 == "rock" or player1 == 'r':
          print("Player 2 won! ")

    elif player2 == 'scissors' or player2 == 's':
        if player1 == "paper" or player1 == 'p':
          print("Player 2 won!")

        elif player1 == "rock" or player1 == 'r':
          print("Player 1 won! ")


    else:
        print('It\'s a tie!')

#checks for valid input
def valid_input(currentInput):
    #list of acceptable inputs
    ace_input = ['paper', 'rock', 'scissors', 'p', 'r', 's']
    valid_entry = False

    """
        changed currentInput.lower() to current input
        and i.lower() to i
    """
    #conditional
    for i in ace_input:
        if currentInput == i:
            valid_entry = True
            break
    if valid_entry == True:
        return valid_entry
    #else:
        #print("error")
        #return False
        #could remove line above
    
#jumps into loop
player1=""
player2=""
#flag = 0
#scoreboard = []

while player1.lower() != "x" or player2.lower() != "x":
    player1 = input("Player 1 enter rock paper or scissors or r p s").lower()
    if valid_input(player1) == True:
        player2 = input("Player 2 enter rock paper or scissors or r p s").lower()
        valid_input(player2)
        if valid_input(player2) == True:
            the_game(player1, player2)
            #prints might not show up because of assignment
        else:
            if player2.lower() == 'x':
                #flag = 1
                break
            print("Try again player 2")
            while player2 != 'x' or valid_input(player2) == False:
                player2 = input("Player 2 enter rock paper or scissors or r p s").lower()
                if valid_input(player2):
                    the_game(player1, player2)
                    break
    else:
        if player1.lower() == 'x':
            break
        print("Try again player 1")
"""
if flag == 1:
    print(flag, "It worked")
print(flag)
"""
print("Goodbye everyone!")
