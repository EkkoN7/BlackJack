import random
from art import ascii_win

def shuffle_cards(deck, amount):
    random_cards = []
    for card in range(amount):
        random_card = random.choice(deck)
        random_cards.append(random_card)
    return random_cards

def count_cards(users_list):
    card_values = []
    total = 0
    for card in users_list:
        split_cards = card.split()
        card_values.append(split_cards[0])
    for values in card_values:
        check_digit = values.isdigit()
        if check_digit == True:
            total += int(values)
        elif values == "Ace" and total +11 <=21:
            total +=11
        elif values == "Ace" and total +11 >21:
            total +=1
        else:
            total +=10
    return total

def blackjack_rules(total_player, player_cards, total_dealer, dealers_cards_complete):
    if int(total_player) <= 21 and int(total_player) > int(total_dealer):
        print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
        print(ascii_win)
        print("You won. Congratz")
        return False
    elif int(total_dealer) <= 21 and int(total_dealer) > int(total_player):
        print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
        print("Game Over")
        return False
    elif int(total_player) == int(total_dealer):
        print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
        print("It is standoff")
        return False
    elif int(total_player) < 21 and int(total_dealer) > 21:
        print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
        print(ascii_win)
        print("You won. Congratz")
        return False
    elif int(total_dealer) < 21 and int(total_player) > 21:
        print(f"Dealer: {dealers_cards_complete}\nPlayer {player_cards} -> Total: {total_player}")
        print("Game Over")
        return False