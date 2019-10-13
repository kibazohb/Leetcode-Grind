#A child is running up to a staircase with n steps and can hop either 1 or 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs
#the approach here is a bit similar to fibonacci series, break it down to sub-problems
#using memoization or caching
#decrementation happens recursively as the number of ways keep going down
def tripleStep(n):
	cache = [-1] *  n  + 1
	
	return countways(n, cache)
	
	def countways(n, arr):
		if n < 0:
			return 0
		elif (n == 0):
			return 	1

		if cache[n] ==  -1:
			cache[n] = countways(n-1, cache) + countways(n-2,cache) + countways(n-3,cache)
			return cache[n]
		else:
			return cache[n] 

	
		
