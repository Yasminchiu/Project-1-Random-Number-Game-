print("Welcome to the Random Number Game!")

import random

name = input("\nFirst things first, what's your name?: ")
score_list = []

def start_game():

    answer = random.randint(1, 10)
    guess = 0
    attempt_count = 0

    while guess != answer:
        
        try:
            guess = int(input("\nOkay {}, guess a number, any number from 1-10: ".format(name)))
        
            if guess not in range(1, 11):
                print("(Oops! This value is outside the range! Please try again.)")
                continue
            
        except ValueError:
            print("(Oops! This is an invalid value. Please try again)")
        
        else:
            if guess > answer:
                print("\nNope! Sorry {}, that wasn't the right number. I'll give you a clue...It's lower than {}!".format(name, guess))
            elif guess < answer:
                print("\nNope! Sorry {}, that wasn't the right number. I'll give you a clue...It's higher than {}!".format(name, guess))
            attempt_count += 1
    else:
        print("\nCongrats {}! You guessed it!\nThat took you a total of {} attempts. Thank's for playing!".format(name, attempt_count))
        score_list.append(attempt_count)
        
start_game()

while True:
    replay = str.lower(input("\nWould you like to play again {}? (Enter yes/no): ".format(name)))
    if replay == 'yes':
        high_score = min(score_list)
        print("\nCURRENT HIGH SCORE = {} attempt/s! \nI wonder if you could beat that...".format(high_score))
        start_game()
    else:
        print("\nThanks for playing the Random Number Game. See you next time {}!".format(name))
        break