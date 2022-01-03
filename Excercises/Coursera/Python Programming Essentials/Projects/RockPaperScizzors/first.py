"""
Implementing RPSLS for Practive project
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
"""

import random

def name_to_number(name):
    """
    New function name_to_number. Takes String as Input
    options (Rock, Spock,Paper,lizard,scissors)
    :param name: 
    :return: integer (0,1,2,3,4)
    """
    if name == 'rock':
        return 0
    elif name == "spock":
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return None

def number_to_name(number):
    """
    New function number_to_name. Takes Integer as Input
    options (Rock, Spock,Paper,lizard,scissors)
    :param name:
    :return: integer (0,1,2,3,4)
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return None

def rpsls(player_choice):
    print("")
    print("Player Choice is ", player_choice, name_to_number(player_choice))
    computer_choice=random.randint(0,4)
    print("Computer Choice is ", number_to_name(computer_choice), computer_choice)

    difference=(name_to_number(player_choice) - computer_choice)%5

    # use if/elif/else to determine winner, print winner message
    if (difference == 1 or difference == 2):
        print("Computer wins!")
    elif (difference == 4 or difference == 3):
        print("Player wins!")
    elif (difference == 0):
        print("Player and computer tie!")


# test your code
rpsls("lizard")
