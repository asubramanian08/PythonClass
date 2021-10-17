# arr1 and arr2 are two sorted arrays
# return sorted array will all elements from arr1 and arr2
def merge(arr1, arr2):
    p1 = p2 = 0
    res = []
    while p1 < len(arr1) or p2 < len(arr2):
        if p1 < len(arr1) and (p2 == len(arr2) or arr2[p1] <= arr2[p2]):
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    return res


# [2, 4, 4, 5, 6, 6, 8, 8, 9, 9, 10, 10, 10, 11]
print(merge([2, 4, 6, 8, 9, 10, 10], [4, 5, 6, 8, 9, 10, 11]))
