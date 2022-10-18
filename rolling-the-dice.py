# libs necessary
from random import randint

# parameter of dice
max = 6
min = 1

roll_again = 'yes'

while (roll_again == 'yes' or roll_again == 'y'):
    print('Rolling the dices...')
    print('The values are...')
    print(randint(min, max))
    print(randint(min, min))

    roll_again = input('Roll the dices again?(yes / no) ')
