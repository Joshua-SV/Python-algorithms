# bubble sort is O(N^2)
def bubbleSort(arr):
    swap = True
    end = len(arr)

    while swap:
        swap = False
        for i in range(1, end):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swap =  True
        end -= 1
    return arr

print(bubbleSort([5,7,3,2,1]))