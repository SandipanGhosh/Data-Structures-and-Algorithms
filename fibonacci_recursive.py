"""Recursive Fibonacci numbers."""
def getFib(position):
	if position == 0 or position == 1:
		return position

	return getFib(position-1) + getFib(position-2)


# Test cases
print(getFib(0))	# prints 0
print(getFib(1))	# prints 1
print(getFib(4))	# prints 3
print(getFib(7))	# prints 13