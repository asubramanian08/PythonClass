def pyramid(x):  # pyramid with x rows
    for i in range(1, x + 1):
        print((x - i) * ' ', end='')
        print(i * '* ')


def cumulativeInfo(arr):  # Sum, Max, Avg of an array
    s = m = a = 0.0
    for ele in arr:
        m = max(m, ele)
        s += ele
    a = s / len(arr)
    print('Sum =', s)
    print('Max =', m)
    print('Avg =', a)


# test
#cumulativeInfo([4, 53, 3.03, 8, -1, True, -4.2])
pyramid(3)
