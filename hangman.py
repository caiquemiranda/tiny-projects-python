# importing the time module
import time

# welcoming the player
name = input('What is your name: ')

print('Hello '+ name, ', time to play hangman!')
print(' ')

# wait 1 sec.
time.sleep(1)

print('Start guessing...')
time.sleep(0.5)

# here we set the secret
word = 'secret'

# creates an variable with an enpty
guesses = ''

# determine the number of turns
turns = 10

# create a while loop

# check if the turns are more than zero
while (turns > 0):

    # make a counter that starts with zero
    failed = 0

    # for ever character in the secret_word
    for char in word:
        
        # see if the character is in the player guess
        if (char in guesses):
            
            # print the out the character
            print(char)

        else:

            # if not found, print a dash
            print('_')

            # and increase the failed counter with one
            failed +=1
        
    # if failed is a equal to zero

    # print you won
    if (failed == 0):
        print('You won!')
    
        # exit the script
        break

    print('')

    # ask the user go guess a character
    
    guess = input('guess a character: ')

    # set the players guess to guesses
    guesses += guess

    # if th guess is not found in the secret word
    if(guess not in word):

        # turn counter decreases with 1 (now 9)
        turns -=1

        print('Wrong')

        # how many turns are left
        print('You are ', + turns, ' more guesses')

        # if the turns are equal to zero
        if (turns == 0):

            # print you lose
            print('You lose.')  