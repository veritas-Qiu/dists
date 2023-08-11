import numpy as np
from itertools import combinations

def calc_color(card):
    return card // 13

def calc_number(card):
    return card % 13

def calc_card_score(cards):
    cards = np.array(cards)
    color = calc_color(cards)
    number = calc_number(cards)
    
    same_color = np.all(color == color[0])
    
    bincount = np.bincount(number)
    ass = np.argsort(bincount, kind = 'stable')
    
    score = 0
    
    if np.min(bincount[-5:]) == 1 and same_color:
        score = 10
    
    elif np.max(bincount) == 4:
        score = 9
    
    elif 3 in bincount and 2 in bincount:
        score = 8
    
    elif same_color:
        score = 7
        
    elif np.min(bincount[-5:]) == 1:
        score = 6
    
    elif np.max(bincount) == 3:
        score = 5
    
    elif np.sum(bincount == 2) == 2:
        score = 4
    
    elif 2 in bincount:
        score = 3
    
    
    if score != 10 and score != 7:
        return [score, ] + np.flip(ass[-5:]).tolist()
    else:
        return [score, ] + sorted(number)[::-1]
        
def compare_some_cards(set_of_cards):
    set_of_cards = np.array(set_of_cards)
    scores = [calc_card_score(cards) for cards in set_of_cards]
    return np.argmax(scores)

def choose_max(cards):
    # choose 5 cards with max score from 7 cards in holdem
    # cards have 7 cards

    outs = list(combinations(cards, 5))

    scores = [calc_card_score(card) for card in outs]
    return max(scores)
    
def visible(cards):
    ans = ''
    color_mark = ['♠', '♥', '♣', '♦']
    for card in cards:
        color = calc_color(card)
        number = calc_number(card)
        ans += f'{color_mark[color]}{number} '
    return ans

if __name__ == '__main__':
    while True:
        cards = np.random.randint(52, size = 7)
        # print(cards)
        # if choose_max(cards)[0] == 8:
        print(visible(cards))
        print(choose_max(cards))
