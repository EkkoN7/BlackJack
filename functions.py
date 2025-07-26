import random

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
