#guessing a random number
def number_guess():

    import random
    rand_num = random.randint(1,10)

    attempts = 0

    for i in range(3, 0, -1):

        user_guess = int(input('Enter your guess: '))
        attempts = attempts + 1

        if user_guess == rand_num:
            print('Your guess is correct')
            print('Total attempts:',attempts)
            break
        elif user_guess < rand_num:
            print('Too low')
        elif user_guess > rand_num:
            print('Too high')

        print('Attempts remaining:', i - 1)

    else:
        print('Game over')
        print('The correct number was', rand_num)

number_guess()