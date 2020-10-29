def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    # player_choice.strip()
    # # random_move = randint(0, 2)
    # moves = ['rock', 'paper', 'scissors']
    computor_choice = input ("enter the move")

    if player_choice == computor_choice:
        print ('Draw!')
    elif(player_choice == 'rock' and computor_choice == 'scissors'):
        win()
    elif player_choice == 'paper' and computor_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computor_choice == 'paper':
        win()
    elif player_choice == 'scissors' and Computor_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computor_choice == 'rock':
        win()
    elif player_choice == "rock" and computor_choice == "paper":
        lose()
    again = input('Do you want to play again? (y or n)')
    if again == 'n':
        break