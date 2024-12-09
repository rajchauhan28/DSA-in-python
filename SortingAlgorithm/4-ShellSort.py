arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def shell(arr: list)-> list:
    """
    Best case : O(1)
    Worst Case: O(N)
    """
    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i
            while j >= distance and arr[j - distance] > temp:
                arr[j] = arr[j - distance]
                j = j-distance
            arr[j] = temp
        distance //= 2
    return arr

print(shell(arr))