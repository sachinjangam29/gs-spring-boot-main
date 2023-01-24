import random

def play_game():
    options = ['rock' , 'paper' , 'scissor']

    comp_choice = random.choice(options)

    user_choice = input("\n Enter the choice 'Rock' , 'Paper' , 'Scissor' ").lower()

    if user_choice == comp_choice:
        print("It is a tie")
    elif user_choice == 'rock' and comp_choice == 'scissor':
        print("You win! Rock beats Scissors !")
    elif user_choice == 'paper' and comp_choice == 'rock':
        print("You win as Paper beats Rock")
    elif user_choice == 'scissor' and comp_choice == 'paper':
        print("You win! because scissor beats paper")
    else:
        print("You lose! {} beats {}.".format(comp_choice,user_choice))


play_game()