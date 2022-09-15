import random
from globals import global_info

class turn():

    def user():
        user_choice = input("\nPlease enter your spot choice: ")

        user_choice = int(user_choice)
        global_info.board[user_choice] = 'X'
        global_info.openSpaces.remove(user_choice)

        try:
            global_info.openSpaces.remove(user_choice)
        except ValueError:
            print("You have selected an invalid space. Please try again. ")

    def comp():
        comp_choice = random.choice(global_info.openSpaces)
        comp_choice = int(comp_choice)
        if global_info.board[comp_choice] == 'X':
            comp_choice = random.choice(global_info.openSpaces)
            global_info.board[comp_choice] = 'O'    
        else:
            global_info.board[comp_choice] = 'O'   
        
        try:
            global_info.openSpaces.remove(comp_choice)
        except ValueError:
            comp_choice = random.choice(global_info.openSpaces)