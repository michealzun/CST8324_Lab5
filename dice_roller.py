#!/usr/bin/python3

"""
    Program name: dice_roller.py
    Program purpose: roll dices
    Author name: yueyang sun
    Date: 5/1/2026
    version number: 1.1
"""


import random;

def get_input(prompt: str) -> int:
    num = 0;
    while(num<=0):
        num = int(input(prompt));
    return num;

def roll():
    #info gathering
    dice_num=get_input("how many dice do you want to roll(enter a none 0): ");
    dice_faces=get_input("how many faces does the dice have(enter a none 0): ");
    
    #calculation
    result_max=dice_num*dice_faces;
    result=random.randint(dice_num,result_max);

    #display result
    if(result==result_max):
        print("congratulations, you've obtain the maximum roll of ", result)
    else:
        print("you've rolled: ", result,". the maximum obtainable is: ", result_max);

def main():
    roll();
    while(input("play again? [Y|N]: ") == "Y"):
        roll();

main();