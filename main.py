from art import deck_of_cards, ascii_art, ascii_win
from functions import shuffle_cards, count_cards, blackjack_rules

print(ascii_art)
is_running = True
dealer_cards = None
player_cards = None
start_game = input("Welcome! Do you want to start a round of Blackjack? Select (S) to begin or (Q) to quit: ").lower().strip()
if start_game == "s":
    dealers_shuffle = shuffle_cards(deck_of_cards, 2)
    players_shuffle = shuffle_cards(deck_of_cards, 2)
    dealers_cards = f"{dealers_shuffle[0]}, face-down card"
    total_dealer = count_cards(dealers_shuffle)
    dealers_cards_complete = f"{dealers_shuffle} -> Total: {total_dealer}"
    player_cards = players_shuffle
    total_player = count_cards(player_cards)
    while is_running:
        if int(total_player) > 21:
            print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
            print ("Game Over")
            is_running = False
        elif int(total_player) == 21 and int(total_dealer) != 21:
            print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
            print(ascii_win)
            print("You won. Congratz")
            is_running = False
        else:
            print(f"Dealer: {dealers_cards}\nPlayer {player_cards} -> Total: {total_player}")
            users_choice = input("Do you want another card? (y/n): ").lower().strip()
            if users_choice == "y":
                new_card = shuffle_cards(deck_of_cards, 1)
                player_cards.append(new_card[0])
                total_player = count_cards(player_cards)
            elif users_choice == "n":
                result = blackjack_rules(total_player, player_cards, total_dealer, dealers_cards_complete)
                if result == False:
                    is_running = False
                else:
                    continue
            else:
                print("Please choose a between (y)es or (n)o.")


elif start_game == "q":
    print ("Goodbye")
    is_running = False
else:
    print("Please enter a valid input.")
