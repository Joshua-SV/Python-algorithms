


def largest(lst):
	# get first value
	large = lst[0]
	# find largest value in list
	for i in range(1,len(lst)):
		if large < lst[i]:
			large = lst[i]
	return large

def two_largest(lst):
	lst = sorted(lst)
	return lst[len(lst)-2:]

print(largest([2,5,9,1,6,7]))

print(two_largest([2,5,9,1,6,7]))

