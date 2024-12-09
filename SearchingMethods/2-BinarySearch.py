arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def binarysearch(arr: list, item: int):
    """
    Worst Case: O(logN)
    """
    
    first = 0
    last = len(arr) - 1
    found = False
    
    while first<=last and not found:
        midpoint = (first + last)//2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

print(binarysearch(arr, 56))
print(binarysearch(arr, 234))
