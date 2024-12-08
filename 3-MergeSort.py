arr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5, 7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]
cnt = 0
def MergeSort(arr: list)->list:
    global cnt
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]
        print(cnt, arr)
        cnt += 1
        MergeSort(left)
        MergeSort(right)

        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                arr[c] = left[a]
                a += 1
                print(a)
            else:
                arr[c] = right[b]
                b += 1

            c += 1
        print(a, b)
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
        
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr

print(MergeSort(arr))