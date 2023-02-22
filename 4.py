#In contrast with the previous problem, this one seems like a bit less of a pain.
from getpass import getpass

def password():
    while True:
        pw = getpass('Password: ')
        if len(pw) >= 8:
            lc = False
            uc = False
            for char in pw:
                if char.isupper():
                    uc = True
                if char.islower():
                    lc = True
            if not uc or not lc:
                print('Your password must contain at least one lower case and one upper case letter')
                continue
        else:
            print('Your password is too short! Please choose another one.')
            continue
        conf = getpass('Confirm password: ')
        if conf != pw:
            print('Your passwords do not match. Please try again.')
            continue

        score = len(pw)/5
        lcs, ucs, dgs, scs = 0, 0, 0, 0
        for char in pw:
            if char.isdigit():
                dgs +=1
            if char.isupper():
                ucs += 1
            if char.islower():
                lcs +=1
            if char in "!@#$%^&*()-+?_=,<>/ ":
                scs += 1
        score += (.3*ucs)+(.5*dgs)+(.7*scs)
        if score < 5:
            rating = 'WEAK'
        elif score < 10:
            rating = 'MEDIUM'
        else:
            rating = 'STRONG'
        if score < 10:
            if input(f'Your password is {rating}. Would you like to choose another one? (y/n) ') == 'y':
                continue
        return pw

with open('4.txt', 'r+') as f:
    content = f.read()
    if content == '':
        print("Looks like you don't have an account. Let's create one!")
        un = input('Username: ')
        content = f'{un}:{password()}'
        f.write(content)
with open('4.txt', 'r+') as f:
    if input('Would you like to change your password? (y/n)') == 'y':
        while True:
            if input('Please enter your username: ') == content.split(':')[0]:
                break
            print('Username not found. Please try again.')
        while True:
            if getpass('Please enter your old password: ') == content.split(':')[1]:
                break
            print('The password is incorrect. Please try again.')
        print("Now let's set up your new password!")
        f.write(f'{content.split(":")[0]}:{password()}')
        print('Password changed!')
