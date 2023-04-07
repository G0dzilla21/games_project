'''
This is the main run file
'''
def main():
    import menu_text
    import game_selection
    replay = "1"
    
    menu_text.menu() #prints the text for the menu


    prompt = game_selection.prompt() #user chooses game or to quit
    

    while prompt == "1" and replay == "1": #checks that you selected to play or replay rps game
        import r_p_s as rps
        import restart
        rps.start_rps() #importing and starting our rock paper scissors game
        replay = restart.replay() #asking to restart game or returns to menu
        
    ##insert while loop for second game here
    
    else:
        if prompt == "q": 
            SystemExit(0) #stops the code from running
        else:
            main() #will restart the main menu
main() 
  