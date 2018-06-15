"""Iterative Fibonacci numbers."""
def getFib(position):
	if position == 0:
		return 0
	if position == 1:
		return 1

	first = 0
	second = 1
	fib = first + second
	counter = 2
	while counter != position:
		first = second
		second = fib
		fib = first + second
		counter += 1

	return fib


# Test cases
print(getFib(0))	# prints 0
print(getFib(1))	# prints 1
print(getFib(4))	# prints 3
print(getFib(7))	# prints 13