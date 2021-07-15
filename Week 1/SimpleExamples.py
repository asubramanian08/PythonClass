# look at PrintWithLoops for the first example
# Note: look at is breifly, there is a lot

# sum an array
arr = [4, 53, 3.03, 8, -1, True, -4.2]
s = 0.0
for ele in arr:
    s = s + ele
print('Sum', '=', s)

# reverse and array
arrLen = len(arr)
for i in range((int)(arrLen / 2)):
    temp = arr[i]
    arr[i] = arr[arrLen - 1 - i]
    arr[arrLen - 1 - i] = temp
print(arr)
