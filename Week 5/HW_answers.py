# %% Min element
def MIN(x, y):
    return x if x < y else y


arr = [3, 54, 72, 2348, 234, 778, 42, 25, 9, 77, 6, 53, 234]
mEle = 0
for ele in arr:
    mEle = MIN(mEle, ele)


# %% Add down
def AddDown(x):
    s = 0
    for i in range(x, 0, -1):
        s += i
    return s


# %% Reverse a string
def reverse1(s):
    newS = ''
    for i in range(len(s)-1, 0, -1):
        newS += s[i]
    return newS


def reverse2(s):
    for i in range(0, len(s)/2):
        temp = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = temp


# %% even list
def EvenList(*ele):
    even = []
    for i in ele:
        if i % 2 == 0:
            even += i
    return even
