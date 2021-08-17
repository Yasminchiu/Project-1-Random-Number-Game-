print("Welcome to the Random Number Game!")

import random

name = input("\nFirst things first, what's your name?: ")
score_list = []

def start_game():
    
    try:
        answer = random.randint(1, 10)
        guess = int(input("Okay {}, guess a number, any number from 1-10: ".format(name)))
        attempt_count = 1
        
        while guess != answer:
            
            if guess not in range(1, 11):
                raise ValueError("Oops! This value is outside the range! Please try again.")
    
            if guess > answer:
                print("\nNope! Sorry {}, that wasn't the right number. I'll give you a clue...It's lower than {}!".format(name, guess))
            elif guess < answer:
                print("\nNope! Sorry {}, that wasn't the right number. I'll give you a clue...It's higher than {}!".format(name, guess))
            guess = int(input("\nLet's try again! Any number from 1-10: "))
            attempt_count += 1
            
    except ValueError as err:
        print("({})".format(err))
    else:
        print("\nCongrats {}! You guessed it!\nThat took you a total of {} attempts. Thank's for playing!".format(name, attempt_count))
        score_list.append(attempt_count)
        
start_game()

while True:
    replay = str.lower(input("\nWould you like to play again {}? (Enter yes/no): ".format(name)))
    if replay == 'yes'and len(score_list) != 0:
        high_score = min(score_list)
        print("\nThe current high score stands at {} attempt/s! I wonder if you could beat that...".format(high_score))
        start_game()
    elif replay == 'yes' and len(score_list) == 0:
        start_game()
    else:
        print("\nOkay {}, see you next time!".format(name))
        break