#!/usr/bin/python3

"""
    Program name: dice_roller.py
    Program purpose: roll dices
    Author name: yueyang sun
    Date: 5/1/2026
    version number: 1
"""


import random;

#info gathering
dice_num = int(input("how many dice do you want to roll(enter a none 0): "));
dice_faces = int(input("how many faces does the dice have(enter a none 0): "));

#calculation
result_max=dice_num*dice_faces;
result=random.randint(dice_num,result_max);

#display result
if(result==result_max):
    print("congratulations, you've obtain the maximum roll of ", result)
else:
    print("you've rolled: ", result,". the maximum obtainable is: ", result_max);