print('Loop syntax,', 'Data structure testing')

print('\nSECTION 1', 'range')
for i in range(9):
    if(i % 3 == 0):
        print(i, end=' ')
print()  # print a new line
for i in range(0, 9, 3):
    print(i, end=' ')
print()  # print a new line

print('\nSECTION 2', 'dict, list, string')
d = {1: 'hello', 2: 'world', 'helloworld': 12}  # dictionary
l = [1, 2]  # list
s = ''  # string
for i in l:
    print(d[i])
    s += d[i]
print()  # print a new line
for ch in s:
    print(ch, end='')
print(d[s])

print('\nSECTION 3', 'while, tuple, set')
t = ('hi', 7, False, 'STOP', 12)  # tuple
st = {4, s, 3.903}  # set
it = 0
while t[it] != False and it < len(t):
    print(t[it], end=' ')
    it += 1
print()  # print a new line
it = 0
for i in st:
    print(i)
while st[it] != False and it < len(st):
    print(st[it], end=' ')
    it += 1
print()
print(st)  # compare with looping version
