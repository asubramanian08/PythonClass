def Hello(name):
    print('Hi ' + name + ', Good morning!')


Hello('James')
Hello('Bob')


def Add(num1, num2):
    # don't always need to print
    return num1 + num2


a = Add(1, 2)
print(Add(2, 3))
print(Add(1, Add(2, 3)))


def Helloworld():
    return "Hello World"


print(Helloworld())
for ch in Helloworld()[::2]:
    print(ch, end='')


def x20():
    x = 20


x = 3
x20()
print(x)  # prints??


def MAX(x, y):
    if x > y:
        return x
    else:
        return y


arr = [6, 4, 5, 7, 8, 8, 6, 4, 332, 345, 34, 63, 574, 53, 4, 56, 5]
count = 0
for i in arr:
    count = MAX(count, i)


def ABS(x):
    if x < 0:
        return -x
    else:
        return x
