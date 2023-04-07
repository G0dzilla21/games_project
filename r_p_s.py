def start_rps():
    import num_players
    import multi_inputs
    import single_inputs
    import rematch
    import timestamp
    
    replay1 = "1" 
    replay2 = "1" #set replays to 1 so loop can run for the first time
     
    wins1 = 0
    wins2 = 0
    draws = 0
    #players = 0
    #computer = 0
    #user = 0
     
    #get the number of players   
    players = num_players.num_players()
    
    
    #start of game loop with 2 players
    while players == "2" and replay1 == "1":
        
        #get the multiplayer inputs
        user1 = multi_inputs.user1()
        user2 = multi_inputs.user2()   
    
        #first compare the two objects to see if there is a draw    
        if user1 == user2:
            print("Draw!")
            draws += 1
        #next compare the 3 different case scenarios    
        elif (user1 == "r") & (user2 == "p"):
            print("User 2 wins!")
            wins2 += 1
        elif (user1 == "p") & (user2 == "s"):
            print("User 2 wins!")
            wins2 += 1
        elif (user1 == "s") & (user2 == "r"):
            print("User 2 wins!")
            wins2 += 1
        #if it's none of the above cases, user 1 must win    
        else:
            print("User 1 wins!")
            wins1 += 1
        
        #asking for a rematch input
        replay1 = rematch.replay1()
    
        
    while players == "1" and replay2 == "1":
        
        #getting our inputs
        user = single_inputs.user()
        computer = single_inputs.computer()
    
        #first compare the two objects to see if there is a draw and add to total draws   
        if user == computer:
            print("Draw!")
            draws += 1
        #next compare the 3 different case scenarios and add to total wins for that winner    
        elif (user == "r") & (computer == "p"):
            print("Computer wins!")
            wins2 += 1
        elif (user == "p") & (computer == "s"):
            print("Computer wins!")
            wins2 += 1
        elif (user == "s") & (computer == "r"):
            print("computer wins!")
            wins2 += 1
        #if it's none of the above cases, user 1 must win    
        else:
            print("User 1 wins!")
            wins1 += 1    
    
        #asking for a rematch input
        replay2 = rematch.replay2()
                    
                      
    #printing out game(s) results        
    if players == "2":
        
        print("\nThanks for playing!")
        print("Draws: ", draws)
        print("User 1 Wins: ", wins1)
        print("User 2 Wins: ", wins2)
        timestamp = timestamp.timestamp()
        
        rps_results = open("rps_results.txt","a")
        rps_results.write(f"Game End: {timestamp} ")
        rps_results.writelines([f"[Draws: {draws},",f" User #1 Wins: {wins1},",f" User #2 Wins: {wins2}]\n"])
        
    if players == "1":
        
        print("\nThanks for playing!")
        print("Draws: ", draws)
        print("User Wins: ", wins1)
        print("Computer Wins: ", wins2)
        timestamp = timestamp.timestamp()
        
        rps_results = open("rps_results.txt","a")
        rps_results.write(f"Game End: {timestamp} ")
        rps_results.writelines([f"[Draws: {draws},",f" User Wins: {wins1},",f" Computer Wins: {wins2}]\n"])
                
       
