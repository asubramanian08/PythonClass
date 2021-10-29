# arr1 and arr2 are two sorted arrays
# return sorted array will all elements from arr1 and arr2
def merge(arr1, arr2):
    p1 = p2 = 0
    res = []
    while p1 < len(arr1) or p2 < len(arr2):
        if p1 < len(arr1) and (p2 == len(arr2) or arr1[p1] <= arr2[p2]):
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    return res

# sort an array using the merge function


def mergesort(arr):
    if len(arr) == 1:
        return arr
    end = int(len(arr)/2)
    arr1 = mergesort(arr[:end])
    arr2 = mergesort(arr[end:])
    return merge(arr1, arr2)


# [-1, 0, 1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8]
print(mergesort([4, 3, 5, 2, 6, 7, 8, 1, -1, 0, 4, 2, 2]))
