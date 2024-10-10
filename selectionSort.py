# Selection Sort is O(N^2)
def selectSort(arr):
	length = len(arr)

	for i in range(length):
		bigNum = arr[0] # have the first value be considered big
		bigIndex = 0
		for j in range(1, length):
			if bigNum < arr[j]:
				bigIndex = j
				bigNum = arr[j]
		# swap the last numbered index with the big number
		arr[bigIndex] = arr[length - 1]
		arr[length - 1] = bigNum
		length -= 1
	return arr

print(selectSort([5,4,3,7,1,2,3,8]))