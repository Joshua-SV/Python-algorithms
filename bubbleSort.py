# bubble sort is O(N^2)
def bubbleSort(arr):
	length = len(arr)
	# Outer loop to go through each pass
	for i in range(length):
		swapped = False
		# Inner loop to compare adjacent elements
		# The range reduces by 'i' with each pass, because the last 'i' elements are already sorted
		for j in range(0, length - i - 1):
			if arr[j] > arr[j + 1]:
				# Swap if elements are in the wrong order
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		# If no elements were swapped, the array is already sorted
		if not swapped:
			break

	return arr

print(bubbleSort([5,7,3,2,1]))