arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

def Insertion1(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i-1
        nxt = arr[i]
        while arr[j] > nxt and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = nxt
        print(f"Pass {i}: {arr}".replace(", ", " -> "))
    return arr

print(f"Array : {arr} \nSorted : {Insertion1(arr)}")
