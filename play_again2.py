def play_game():
    while True:
        user_input = raw_input('Do you want to play again (Y or N)? ').upper()
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False
        else:
            return 'Invalid input'
            
print play_game()
