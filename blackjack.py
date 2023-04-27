from art import logo
import random
import os
# could make this a dictionary, i.e. 'jack': 10

# Ace is always 11
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "You lose, computer has Black Jack."
    elif user_score == 0:
        return "You win. You have Black Jack!"
    elif user_score > 21:
        return "Bust, you lose."
    elif comp_score > 21:
        return "Computer bust, you win!"
    elif user_score > comp_score:
        return "You win!"
    elif comp_score > user_score:
        return "You lose."

def play_game():        
    print(logo)
    user_cards = []
    comp_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f'Your cards:\n\t{user_cards}\nCurrent score:\n\t{user_score}')
        print(f'Computer show card:\n\t{comp_cards[0]}\n')

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            add_card = input('Another card (Y/N)?\n')

            if add_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)
        
    print(f'Your hand:\n\t{user_cards}\nCurrent score:\n\t{user_score}')
    print(f'Computer hand:\n\t{comp_cards}\nComputer score:\n\t{comp_score}\n')
    print(compare(user_score, comp_score))

while input('Play Black Jack (Y/N)?\n') == 'y':
    os.system('clear')
    play_game()

print('Thanks for playing!')