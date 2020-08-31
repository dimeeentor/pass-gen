import random

alphabet = (
    'A', 'a',
    'B', 'b',
    'C', 'c',
    'D', 'd',
    'E', 'e',
    'F', 'f',
    'G', 'g',
    'H', 'h',
    'I', 'i',
    'J', 'j',
    'K', 'k',
    'L', 'l',
    'M', 'm',
    'N', 'n',
    'O', 'o',
    'P', 'p',
    'Q', 'q',
    'R', 'r',
    'S', 's',
    'T', 't',
    'U', 'u',
    'V', 'v',
    'W', 'w',
    'X', 'x',
    'Y', 'y',
    'Z', 'z'
)
numbers = ('1', '2', '3', '4', '5', '6', '7','8', '9', '0')
symbols = ('!', '@', '#', '$', '&', '(', ')', '<', '>', ',', '.', '/')
password = []

print('Welcome to the PassGen.')

while True:
    try:
        pass_len = 0
        length = int(input('Enter a lenght of your password: '))
    except ValueError:
        print('You accidentaly typed a letter.')
        continue
    if length >= 6:
        print('Better to choose random.')
        rand = input('Do you wanna make random varibles?: ')
        if rand == 'yes' or rand == 'Yes':
            while len(password) < length:
                password.append(alphabet[random.randint(0, len(alphabet) - 1)])
                password.append(numbers[random.randint(0, len(numbers) - 1)])
                password.append(symbols[random.randint(0, len(symbols) - 1)])
            set(password)
            print('Here is your password:', str(''.join(password)))
            input('Press enter to exit.')
            break
        elif rand == 'no' or rand == 'No':
            try:
                letter = int(input('Enter how many letters you want to have in your password: '))
                pass_len += letter
            except ValueError:
                print('You wrote a letter instead of a number.')
                continue
            try:
                number = int(input('Enter how many numbers you want to have: '))
                pass_len += number
            except ValueError:
                print('You wrote a letter instead of a number.')
                continue
            try:
                symbol = int(input('Enter how many special symbols you want to have: '))
                pass_len += symbol
            except ValueError:
                print('You wrote a letter instead of a number.')
                continue
            if pass_len > length:
                print('You cannot use more symbols than you wrote.')
                continue
            elif pass_len <= length:
                while len(password) < length:
                    while number > 0:
                        password.append(numbers[random.randint(0, len(numbers) - 1)])
                        number -= 1
                    while letter > 0:
                        password.append(alphabet[random.randint(0, len(alphabet) - 1)])
                        letter -= 1
                    while symbol > 0:
                        password.append(symbols[random.randint(0, len(symbols) - 1)])
                        symbol -= 1
                    set(password)
                print('Your password: ' + str(''.join(password)))
                input('Press enter to exit.')
                break
        else:
            print('You made a mistake.')
            continue
        break
    else:
        print('Nope, min number is 6')