defArr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]
print("List : ", defArr)
# first method
for j in range(len(defArr)):
    for i in range(len(defArr)-1):
        while defArr[i] > defArr[i+1]: 
                defArr[i], defArr[i+1] = defArr[i+1], defArr[i]
    print(j,":", defArr)

defArr = [7, 3, 5, 6, 2, 1, 34, 4,5, 4,56, 567, 7, 67, 5]

# Second Method
def BubbleSort(defArr: list) -> list:
    for j in range(len(defArr)- 1, 0, -1):
        for i in range(len(defArr)-1):
            if defArr[i] > defArr[i+1]: 
                    defArr[i], defArr[i+1] = defArr[i+1], defArr[i]
    return defArr
print("second method :", BubbleSort(defArr))