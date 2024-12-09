arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def interpolationsearch(arr: list, x: int):
    arr.sort()
    idx0 = 0
    idxn = (len(arr) - 1)
    found = False
    while idx0 <= idxn and x >= arr[idx0] and x <= arr[idxn]:
        # Find the mid point
            mid = idx0 +int(((float(idxn - idx0)/( arr[idxn] - arr[idx0])) *
    ( x - arr[idx0])))
            if arr[mid] == x:
                found = True
                return found
    if arr[mid] < x:
            idx0 = mid + 1
    return found

print(interpolationsearch(arr, 40))
print(interpolationsearch(arr, 56))