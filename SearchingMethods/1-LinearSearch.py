arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def linearsearch(arr: list, item: int):
    """
    Worst Case: O(N)
    """
    idx = 0
    found = False

    while idx < len(arr) and found is False:
        if arr[idx] == item:
            found = True
        else:
            idx += 1
    return f"Found {item} at index {idx}" if found else found

print(linearsearch(arr, 10))
print(linearsearch(arr, 1))