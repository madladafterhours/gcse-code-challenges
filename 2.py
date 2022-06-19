#The program will keep requesting inputs until you either write "done" or "quit"
#If you'd like to open an existing set of integers, use the '--fromsave' argument

import sys
from collections import Counter
x=True
numlist = []
if len(sys.argv) > 1:
    if sys.argv[1] == '--fromsave':
        x = False
        with open('2.txt', 'r') as f:
            numlist = [int(num) for num in f.read()[:-1].split(' ')]

while x == True:
    num = input()
    if num.lower() == 'done':
        if input('Save? ').lower() == 'yes':
            save = ''
            for number in numlist:
                save += str(number)+' '
            with open('2.txt', 'w') as f:
                f.write(save)
        break
    elif num.lower() == 'quit':
        quit()
    numlist.append(int(num))

type = input('What property to calculate? (mean, median, mode)? ')
if type == 'mean':
    result = sum(numlist)/len(numlist)
elif type == 'median':
    if len(numlist)%2 != 0:
        result = sorted(numlist)[int((len(numlist)-1)/2)]
    else:
        result = (sorted(numlist)[int((len(numlist)-1)/2)]+sorted(numlist)[(int((len(numlist)-1)/2)+1)])/2
elif type == 'mode':
    result = Counter(numlist).most_common(1)[0][0]
print(f'The {type} value is: {result}')