# binary search
# run time O(log N)

def binaryS(lst, target):
	low = 0
	high = len(lst) - 1

	while low <= high:
		# do floor division // 2 to get the mid index
		mid = (low + high) // 2
		guess = lst[mid]

		if guess == target:
			# if the guess is correct return index
			return mid
		elif guess < target:
			low = mid + 1
		else:
			high = mid - 1
	# if search is unsuccessful return nil
	return None

lst = [3,5,7,8,9,10,11,12,13,14,15,16]
index = binaryS(lst, 16)
print(f"the number {lst[index]} is at index {index}")