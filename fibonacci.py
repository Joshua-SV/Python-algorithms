def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	firstPrev = 0
	secondPrev = 1
	sum = 0

	while n > 1:
		sum = firstPrev + secondPrev
		firstPrev = secondPrev
		secondPrev = sum
		n -= 1
	return sum

print(fib(6))