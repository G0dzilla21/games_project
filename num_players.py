# -*- coding: utf-8 -*-
'''
This module asks the number of players for the game
'''
def num_players():
    
    players = input("How many players (1 or 2): ")
    
    while (players != "1" and players != "2"):
        players = input("Invalid input! How many players (1 or 2): ")
    return players;        
    