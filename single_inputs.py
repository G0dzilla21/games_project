# -*- coding: utf-8 -*-
def user():
    user = input("User 1: Enter 'r' for rock, 'p' for paper, or 's' for scissors: ") 
    while (user != "r" and user != "p" and user != "s"): #ensuring the user's input is correct
        user = input("That is not a valid input, please re-enter: ")
    return user;

def computer():
    import random
    
    computer = random.randrange(1, 4)  #this block gets a random number 1-3 and assigns it to computer
    if computer == 1:                  #then assigning computer a character (r,p,s) based off the random number
        computer = 'r'
    elif computer == 2:
        computer = 'p'
    else: 
        computer == 's'
    return computer; 