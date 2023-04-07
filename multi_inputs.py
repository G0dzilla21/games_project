def get_user_input(user):
    user1 = input(f"User {user}: Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    while (user1 != "r" and user1 != "p" and user1 != "s"): #ensuring the user's input is correct
        user1 = input("That is not a valid input, please re-enter: ")
    return user1;
    
'''   #OLD CODE (WAS COMBINED INTO ONE FUNCTION) 
def user1():
    user1 = input("User 1: Enter 'r' for rock, 'p' for paper, or 's' for scissors: ") 
    while (user1 != "r" and user1 != "p" and user1 != "s"): #ensuring the user's input is correct
        user1 = input("That is not a valid input, please re-enter: ")
    return user1;

def user2():
    user2 = input("User 2: Enter 'r' for rock, 'p' for paper, or 's' for scissors: ") 
    while (user2 != "r" and user2 != "p" and user2 != "s"): #ensuring the user's input is correct
        user2 = input("That is not a valid input, please re-enter: ") 
    
    return user2;        
'''