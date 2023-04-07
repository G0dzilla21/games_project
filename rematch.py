# -*- coding: utf-8 -*-

def replay1():
    replay1 = input("Rematch? 1 for yes, 2 for no: ") #asking to play again
    while replay1 != "1" and replay1 != "2": #ensuring the user's input is correct
        print("Invalid input.")
        replay1 = input("Rematch? 1 for yes, 2 for no: ")
    return replay1;


def replay2():
    replay2 = input("Rematch? 1 for yes, 2 for no: ") #asking to play again
    while replay2 != "1" and replay2 != "2": #ensuring the user's input is correct
        print("Invalid input.")
        replay2 = input("Rematch? 1 for yes, 2 for no: ")
    return replay2;
