# add x + ... + 1 (order of addition matters)
def addDown(x):
    ans = 0
    for i in range(x, 0, -1):
        ans += i
    return ans


# count even numbers
num = 1
count = 0
while num != 0:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        count = count + 1
print('The number of even numbers entered is', count)
