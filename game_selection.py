# -*- coding: utf-8 -*-
'''
Asks for users input for which game to play on the main menu or to quit the program
'''
def prompt():
    prompt = input("Please make a selection: ")
    while prompt != "1" and prompt != "q":
            prompt = input("Invalid input. Please make a selection: ")
    return prompt;