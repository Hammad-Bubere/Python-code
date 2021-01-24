n=18
number_of_guesses=1
print('Number of guesses is limited to only 9 times:')
while (number_of_guesses<=9):
    guesses_number = int(input('Guess the number :\n'))
    if guesses_number<18:
        print('you enter less number enter greater number.\n')
    elif guesses_number>18:
        print('you enter greater number please enter smaller number.\n')
    else:
        print('you win')
        print(number_of_guesses,'number of guesses you took to finish.')
        break
    print(9-number_of_guesses,'no of guesses left')
    number_of_guesses = number_of_guesses + 1
    if (number_of_guesses>9):
        print('game over')