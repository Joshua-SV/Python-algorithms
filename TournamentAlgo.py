# using the tournament to find 2 highest value in a list

# function which takes a list() of divisible by 2 length
def tournament(lst):
	length = len(lst)

	# create empty lists
	winners = [None] * (length - 1)
	losers = [None] * (length - 1)
	priorMatch = [-1] * (length - 1)


	index = 0
	# eliminate numbers based on adjacent comparing, first round
	for i in range(0, length, 2):
		if lst[i] < lst[i + 1]:
			winners[index] = lst[i + 1]
			losers[index] = lst[i]
		else:
			winners[index] = lst[i]
			losers[index] = lst[i + 1]
		index += 1

	# eliminate numbers of winners bracket
	subscript = 0
	while index < length - 1:
		if winners[subscript] < winners[subscript + 1]:
			winners[index] = winners[subscript + 1]
			losers[index] = winners[subscript]
			priorMatch[index] = subscript + 1
		else:
			winners[index] = winners[subscript]
			losers[index] = winners[subscript + 1]
			priorMatch[index] = subscript
		subscript += 2
		index += 1

	#find largest and second largest
	largest = winners[subscript]
	second = losers[subscript]
	subscript = priorMatch[subscript]
	while subscript >= 0:
		if second < losers[subscript]:
			second = losers[subscript]
		subscript = priorMatch[subscript]

	return (largest,second)

l = [2,3,10,5,7,9,0,24,1,11,12,14]
print(tournament(l))