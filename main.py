def main():
    import menu_text
    import game_selection
    replay = "1"
    
    menu_text.menu()


    prompt = game_selection.prompt() #user chooses game or to quit
    

    while prompt == "1" and replay == "1":
        import r_p_s as rps
        import restart
        rps.start_rps() #importing and starting our rock paper scissors game
        replay = restart.replay() #asking to restart game or returns to menu
        
    ##insert while loop for second game here
    
    else:
        if prompt == "q":
            SystemExit(0)
        else:
            main()
main() 
  