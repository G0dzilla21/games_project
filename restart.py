# -*- coding: utf-8 -*-

def replay():
    replay = input("\nWould you like to restart rock, paper, scissors? 1 for yes, 2 for no: ")
     #ensuring the user's input is correct
    while replay != "1" and replay != "2":
        replay = input("\nInvalid input. Would you like to restart rock, paper, scissors? 1 for yes, 2 for no: ")
        print('')
    return replay;
