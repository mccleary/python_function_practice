def play_game():
    user_input = raw_input('Do you want to play again (Y or N)? ').upper()
    if user_input == 'Y':
        return True

    else:
        return False
print play_game()
