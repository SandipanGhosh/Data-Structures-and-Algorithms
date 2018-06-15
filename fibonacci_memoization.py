class Fib(object):
	
	def __init__(self):
		self.memo = {}

	def fib(self, n):

		if n < 0:
			raise IndexError('Negative index', 'No negative index in a series.')

		if n in [0,1]:
			return n;

		if n in self.memo:
			print "grabbing memo[{}]".format(n)
			return self.memo[n]

		print "computing fib[{}]".format(n)
		result = self.fib(n-1) + fib(n-2)

		self.memo[n] = result

		return result

