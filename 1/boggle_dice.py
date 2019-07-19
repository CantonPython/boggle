#!/usr/bin/python3

import random
import string

# The faces for 6 sidied boggle dice.
# Note that 'q' implies 'qu'.
DICE = [
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
    'abjmoq',
    'egintv',
]

def shake(number=16):
   """Roll the dice."""
   shaken = []
   dice_ = list(DICE)  # Make a copy so we can shuffle it.
   random.shuffle(dice_)
   for d in dice_[0:number]:
       letter = random.choice(d)
       shaken.append(letter)
   return shaken

def main():
    results = shake()
    print(results)

if __name__ == '__main__':
    main()
