from art import logo
import random

print(logo)

your_card = []
computer_card = []

def pay_card():
    for i in range(0,2):
        your_card.append(random.randint(1,13))
        computer_card.append(random.randint(1,13))

def cal_score(card):
    score = 0
    for i in range(len(card)):
        if card[i] > 10:
            card[i] = 10
        if card[i] == 1:
            card[i] = 11
        score += card[i]
    if score > 21:
        for i in range(len(card)):
            if card[i] == 1:
                card[i] = 1
            score += card[i]
    return score
        
    

pay_card()
print(your_card)
print(computer_card)
print(cal_score(your_card))
print(cal_score(computer_card))