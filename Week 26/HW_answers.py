def linearContains(arr, x):
    for i in arr:
        if i == x:
            return True
    return False


def addBack(arr, x):
    if len(arr) == 0 or arr[len(arr) - 1] <= x:
        arr.append(x)


def binaryContains(arr, x):
    lo = 0
    hi = len(arr) - 1
    while (lo <= hi):
        mid = int((lo + hi) / 2)
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return True
    return False


arr = []
print("arr:", arr)
print("Contains 4:", linearContains(arr, 4))
print("Adding 7")
addBack(arr, 7)
print("Contains 7:", linearContains(arr, 7))
print("Adding -1")
addBack(arr, -1)
print("Contains -1:", linearContains(arr, -1))
print("arr:", arr)
print("Length:", len(arr))
print("Adding 10, -11, 12")
addBack(arr, 10)
addBack(arr, -11)
addBack(arr, 12)
print("arr:", arr)
print("Contains 20:", linearContains(arr, 20))
print("Length:", len(arr))
print("arr:", arr)
