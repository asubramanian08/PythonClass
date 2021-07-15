# rock, paper, scissors
import random
computer = 0
user = 0
options = ['rock', 'paper', 'scissors']
while computer == user:
    computer = random.randint(0, 2)
    user = int(input('Enter 0-' + options[0]
                     + ', 1-' + options[1]
                     + ',or 2-' + options[2] + ': '))
    if user > 2 or user < 0:
        user = computer
        continue
    if (computer + 1) % 3 == user:
        print('You won!', end=' ')
    elif (user + 1) % 3 == computer:
        print('You lost!', end=' ')
    else:
        print('Its a tie, try again', end=' ')
    print('You entered ' + options[user] +
          ', The computer picked ' + options[computer])
print('Game finished\n')

# count digits
num = int(input('Enter a large number: '))
digits = 0
while num > 0:
    num //= 10
    #num = int(num / 10)
    digits += 1
print('You number has', digits, 'digits')
