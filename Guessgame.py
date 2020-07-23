import random
import os
import time


while True:
    Decrease = 7
    os.system('cls||clear')
    print("\nI'm thinking of a number between 1 to 20 ,and you will get 7 tries to guess the coreect number\n")
    secret_number = random.randrange(1, 20)
    try:
        for i in range(1, 8):
            guess = int(
                input("=>"))

            if guess > secret_number:
                print(f"Your guess is higher.Type again {7-i} tries left\n")

            elif guess < secret_number:
                print(f"Your guess is lower.Type again {7-i} tries left\n")

            elif guess == secret_number:
                print('========================================================\n')
                print(
                    f'Gooodjob! Your guess is correct.You did it in {i} tries.\n')
                print('========================================================\n')
                break

        if guess != secret_number:
            print('--------------------------------------------------')
            print(
                f"sorry correct number is {secret_number}.\nThanks for playing Guess The Number")
            print('--------------------------------------------------\n')

        print('If you want to play more than type "play" or type "exit"')
        Take = input('>')

        if Take == 'play':
            pass
        elif Take == 'exit':
            break

    except:
        print('   Invalid argument')
        time.sleep(1)
