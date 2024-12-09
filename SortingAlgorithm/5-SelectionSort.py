arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def selectionsort(arr: list)-> list:
    """
    Worst Case: O(N^2)
    """
    for slot in range(len(arr) - 1, 0, -1):
        maxIdx = 0
        for location in range(1, slot + 1):
            if arr[location] > arr[maxIdx]:
                maxIdx = location
        arr[slot], arr[maxIdx] = arr[maxIdx], arr[slot]
    return arr

print(selectionsort(arr))