# Game Flipflop
import random

def coin_flip():
    if random.random() >=0.5: #random.random is use for float
        return 'Head'
    else:
        return 'Tail'
print(coin_flip())