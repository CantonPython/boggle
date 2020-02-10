#!/usr/bin/python3

import random

class BoggleDice:

    # Faces of the 6-sided boggle dice, 16 of them.
    dice = [
        'ednosw',
        'aaciot',
        'acelrs',
        'ehinps',
        'eefhiy',
        'elpstu',
        'acdemp',
        'gilruw',
        'egkluy',
        'ahmors',
        'abilty',
        'adenvz',
        'bfiorx',
        'dknotu',
        'abjmoq', # The letter 'q' implies the pair 'qu'.
        'egintv',
    ]

    def shake(self):
       letters = []
       dice = list(self.dice) # Make a copy to be shuffled in place.
       random.shuffle(dice)
       for d in dice:
           letter = random.choice(d)
           letters.append(letter)
       return ''.join(letters)
