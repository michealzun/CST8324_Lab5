#!/usr/bin/python3

"""
    Program name: dice_roller.py
    Program purpose: roll dices
    Author name: yueyang sun
    Date: 5/1/2026
    version number: 1.2
"""


import random;

#input number of dice
def get_numdice() -> int:
    num_dice = 0;
    while(num_dice<=0):
        num_dice = int(input("how many dice do you want to roll(enter a none 0): "));
    return num_dice;

#input number of faces
def get_diefaces() -> int:
    num_faces = 0;
    while(num_faces<=0):
        num_faces = int(input("how many faces does the dice have(enter a none 0): "));
    return num_faces;

#generate sum
def roll_dice(num_dice: int, num_face: int) -> int:
    max=num_dice*num_face;
    return random.randint(num_dice,max);

#check if rolled max
def is_max_score(roll: int, max: int) -> bool:
    return (roll == max);

#perform a roll
def roll():
    #info gathering
    dice_num=get_numdice();
    dice_faces=get_diefaces();
    
    #calculation
    result_max=dice_num*dice_faces;
    result=roll_dice(dice_num,dice_faces);

    #display result
    if(is_max_score(result,result_max)):
        print("congratulations, you've obtain the maximum roll of ", result)
    else:
        print("you've rolled: ", result,". the maximum obtainable is: ", result_max);

#run roll, prompt to roll again
def main():
    roll();
    while(input("play again? [Y|N]: ").upper() == "Y"):
        roll();

main();