import random
import os
import time


#Screen clear command
clear = lambda: os.system('clear')


logo = '''
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/
'''
cards =  [
("----------",
 "|A       |",
 "|   /\   |",
 "|  /  \  |",
 "| (    ) |",
 "|  /__\  |",
 "|       A|",
 "----------",),
("----------",
 "|2       |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|       2|",
 "----------"),
("----------",
 "|3       |",
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       3|",
 "----------"),
("----------",
 "|4       |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|       4|",
 "----------"),
("----------",
 "|5       |",
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       5|",
 "----------"),
("----------",
 "|6       |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|       6|",
 "----------"),
("----------",
 "|7       |",
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       7|",
 "----------"),
("----------",
 "|8       |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|       8|",
 "----------"),
("----------",
 "|9       |",
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       9|",
 "----------"),
("----------",
 "|10      |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|      10|",
 "----------"),
("----------",
 "|J       |",
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       J|",
 "----------"),
("----------",
 "| K      |",   
 "|  _  _  |",
 "| ( \/ ) |",
 "|  \  /  |",
 "|   \/   |",
 "|       K|",
 "----------"),
("----------",
 "|Q       |",
 "|   /\   |",
 "|  /  \  |",
 "|  \  /  |",
 "|   \/   |",
 "|       Q|",
 "-----------")]

     
my_hand = []
de_hand = []




# This function is used to create your cards, it creates cards for both my_hand and de_hand based on the parameter you give.
# You can also change the number of cards to be created with the first parameter called num_of_cards.

def create_cards(num_of_cards, for_who):
    global de_hand, my_hand
    card = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=num_of_cards)    # Choose a random card, num_of_cards stands for how many cards to choose.
    
    if for_who == my_hand:                                                    # This function creates cards and places them to the hand you choose,
        my_hand.extend(card)                                                  # the parameter for_who will deretmine where it goes.

    if for_who == de_hand:
        de_hand.extend(card)                                                                         






# This function prints out the cards in your hand or in the dealers hand. You have to specify the parameter to
# get your desired results as output.

def print_card(for_who):
    person_deck = ''

    if for_who == my_hand:                       # The if statements are here to determine whos card deck
        person_deck = my_hand                    # you want to print out.

    elif for_who == de_hand:
        person_deck = de_hand


    for i in range(8):  # 8 is the height of the card.
        for y in person_deck:
            # Now get the corresponding card in the my_hand list
            # and print its first line, then the first line of
            # the next die and so on.
            print(cards[y-1][i], end=' ')
        print()







# Here are the actions in definitions that you can perform:

# Pulling action - pulling a random card then printing it.:
def pull_card(for_who):
    if for_who == my_hand:                     # This function makes it easier to pull cards, you just
        create_cards(1, my_hand)               # need to specify for who you want to pull the cards for.
    
    if for_who == de_hand:
        create_cards(1, de_hand)

    clear()     # Clean the screen so we can pull a card and add it to the already existing ones and print them out.

    print_card(de_hand)
    print(f'Dealer Hand Value: {sum(de_hand)}')
    print_card(my_hand)
    print(f'Your Hand Value: {sum(my_hand)}')
    





# The game starts here, every other function is working within the start_game(): function
# if you run it it will automatically call the other functions.

def start_game():
    clear()
# Stage 1: Starting with 1 card on dealers side and 2 on your side.
    pull_card(my_hand)
    pull_card(my_hand)
    pull_card(de_hand)

# Stage 2: Starting the actions input, choose what to do.
    while True:
        action = input('\n(H)it, (S)tand: ')

    # Action code for pulling a card with logical operators involved.   
        if action.lower() == 'h':
            pull_card(my_hand)

            if sum(my_hand) > 21:
                print('You lost!')
                time.sleep(2)
                break

            elif sum(my_hand) == 21:               # These are the conditions for pulling, if you go trough
                print('BlackJack')
                time.sleep(2)                      # them the program will break from the loop and it will
                break                              # kick you back to the menu.

            elif sum(de_hand) >= 21:
                print('You won!')
                time.sleep(2)
                break


    # Actions code for staying with logical operators involved.            
        elif action.lower() == 's':
            while sum(de_hand) < sum(my_hand):
                time.sleep(1.5)
                pull_card(de_hand)

            if sum(de_hand) > 21:
                print('You won!')
                time.sleep(2)
                break 

            elif sum(de_hand) == sum(my_hand):           # These are the conditions for pulling, if you go trough
                print('It\'s a draw')
                time.sleep(2)                            # them the program will break from the loop and it will
                break                                    # kick you back to the menu.
                    
            else:
                print('You lost')
                time.sleep(2)
                break


        else:
            print('Invalid input!')
    
    


while True:
    clear()
    print(logo)
    action = input('Do you wish to start the game? (y/n): ')
    if action == 'y':
        my_hand = []
        de_hand = []
        start_game()
    elif action == 'n':
        print('Ok, bye!')
        break
    else:
        print('Invalid input!')
        time.sleep(1.5)
        continue


