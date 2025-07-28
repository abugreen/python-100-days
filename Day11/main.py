import random
from art import logo


def deal_card():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calcuate_score(cards):
    if sum(cards) == 21 and len(cards) == 2 :
        return 0

    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score , computer_score):
    if user_score == computer_score :
        return "draw"
    elif computer_score == 0 :
        return "loss , opponent has blackjack"
    elif user_score == 0 :
        return "win with a blackjack"
    elif user_score > 21 :
        return "you went over , you loss"
    elif computer_score > 21 :
        return "opponent wnet over , you win"
    elif user_score > computer_score :
        return "you win"
    else :
        return "you lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    while not is_game_over :
        user_score = calcuate_score(user_cards)
        computer_score = calcuate_score(computer_cards)

        print(f"Your cards is {user_cards}, socre is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0 :
            is_game_over = True
        else :
            user_shold_deal = input("type 'y' to get another card , type 'n' to pass\n")
            if user_shold_deal == "y" :
                user_cards.append(deal_card())
            elif user_shold_deal == "n" :
                is_game_over = True
            

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calcuate_score(computer_cards)
    

    print(f"your final hand : {user_cards}, final score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score , computer_score))

while input("do you want to play a game of blackjack? type 'y' or 'n' :") == "y" :
    print("\n"*20)
    play_game()