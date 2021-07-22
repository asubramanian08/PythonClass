# check if a number is prime
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, num):  # cleaner to start at 2
    if num % i == 0:
        is_prime = False
        # could break but don't need to
if is_prime:
    print("The number entered is prime")
else:
    print("The number entered is not prime")

#replace vowels with #
s = input('Enter a string: ')
newS = ''
vowels = 'aeiou'
for ch in s:
    if (ch in vowels):
        newS += '#'
    else:
        newS += ch
print('The new string: ' + newS)
# or with replace
s = input('Enter a string: ')
vowels = 'aeiou'
for ch in vowels:
    s = s.replace(ch, '#')
print('The new string: ' + newS)

# every other char in a string
s = input('Enter a string: ')
print('Every other letter is:', end=' ')
for i in range(0, len(s), 2):
    print(s[i], end='')
print()
