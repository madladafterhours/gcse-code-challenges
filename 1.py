#To set the difficulty, use the '--difficulty' argument (e.g. --difficulty easy)

from random import randint
import sys
import time

difficulty = 'normal'
if len(sys.argv) > 1:
    difficulty = sys.argv[2]
multiplier = 0.75 if difficulty == 'easy' else 1.25 if difficulty == 'hard' else 1

number = randint(10000, 99999) if difficulty == 'hard' else randint(1000, 9999)
number_separated = [int(x) for x in str(number)]

start_time = time.time()
attempts = 0

while True:
    attempts +=1 
    correct_guesses = []
    response = 'Wrong. '
    guess = int(input(f'Guess the {len(str(number))} integer number: '))
    guess_separated = [int(x) for x in str(guess)]
    
    if guess == number:
        break
    for index, integer in enumerate(guess_separated):
        if integer == number_separated[index]:
            correct_guesses.append(integer)
    if len(correct_guesses) == 0:
        response+="You didn't guess any integers correctly."
    elif difficulty == 'easy':
        response += 'Correct guesses: '
        for integer in correct_guesses:
            response += f'\nNumber {integer} in position {number_separated.index(integer)}'
    else:
        response += 'Correct guesses: '
        for integer in correct_guesses:
            response += f'\nNumber {integer}'
    print(response+'\n')
                
score = int(((1000000/attempts)/(time.time()-start_time))*multiplier)
print(f'Correct! The number is {number}! Your score is {score}.\n')

username = input('Username: ')

with open('1scores.txt', 'r') as f:
    scorelist = f.readlines()
with open('1scores.txt', 'w') as f:
    exists = False
    if len(scorelist) > 0:
        f.write(username+':'+str(score)+'\n')
        for combo in scorelist:
            if combo.split(':')[0] == 'username':
                exists = True
                if int(combo.split(':')[1]) < score:
                    f.write(username+':'+str(score)+'\n')
                else:
                    f.write(combo+'\n')
            else:
                f.write(combo+'\n')
        if not exists:
            f.write(username+':'+str(score)+'\n')
    else:
        f.write(username+':'+str(score)+'\n')

with open('1scores.txt', 'r') as f:
    lines = f.readlines()
    #Here comes what is likely the most convoluted line of code I've ever written
    #What the following line does is: splits the raw string combos and converts them into dictionary pairs and sorts them by score
    leaderboard = {user: score for user, score in reversed(sorted(dict(zip([user.split(':')[0] for user in lines if user !='\n'], [score.split(':')[1] for score in lines if score !='\n'])).items(), key=lambda item: item[1]))}

i = 0
print('\nLeaderboard: ')
for user, score in leaderboard.items():
    i +=1 
    newline = '\n' #Python bug(?)
    #Despite following proper syntax, the backslash in '\n' still conflicts with the f formatting expression 
    print(f'#{i} {user}, {score.replace(newline, "")}')