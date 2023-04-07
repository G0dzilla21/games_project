# -*- coding: utf-8 -*-

def prompt():
    prompt = input("Please make a selection: ")
    while prompt != "1" and prompt != "q":
            prompt = input("Invalid input. Please make a selection: ")
    return prompt;