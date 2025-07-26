import os
import random
from art import deck_of_cards
from functions import shuffle_cards, count_cards
from Framework import frame_input

#print(ascii_art)
is_running = True
while is_running:
    start_game = input("Welcome to PyCasino! Do you want to start a round of Blackjack? Select (S) to begin or (Q) to quit: ").lower().strip()
    if start_game == "s":
        dealers_shuffle = shuffle_cards(deck_of_cards, 2)
        #dealers_cards.append(dealers_shuffle)
        players_shuffle = shuffle_cards(deck_of_cards, 2)
        #player_cards.append(players_shuffle)
        dealers_cards = f"{dealers_shuffle[0]}, face-down card"
        player_cards = players_shuffle
        total_player = count_cards(player_cards)
        if int(total_player) > 21:
            print ("Game Over")
        elif int(total_player) == 21:
            print ("You won. Congratz")
        else:
            print(f"Dealer: {dealers_cards}\nPlayer {player_cards} -> Total: {total_player}")


    elif start_game == "q":
        print ("Goodbye")
        is_running = False
    else:
        print("Please enter a valid input.")
