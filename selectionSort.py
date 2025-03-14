# Selection Sort is O(N^2)
def selectionSort(arr, sort="des"):
    length = len(arr)

    for i in range(length):
        bigIndex = i  # Start by assuming the first unsorted element is the largest

        for j in range(i + 1, length):
            if sort.lower() == "ascd":
                if arr[j] < arr[bigIndex]:  # Find the low element
                    bigIndex = j
            else:
                if arr[j] > arr[bigIndex]:  # Find the max element
                    bigIndex = j
        # Swap the found max element with the first unsorted element
        arr[i], arr[bigIndex] = arr[bigIndex], arr[i]
    return arr

print(selectionSort([5,4,3,7,1,2,3,8]))