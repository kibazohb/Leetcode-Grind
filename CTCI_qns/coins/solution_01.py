#solution to coins question on cracking the coding interveiw
#using recursion and dynamic programming
#for any amount, for instance 150 cents
# we start with the largest coin in the change list 
# then from the largest coin, see if the possiblities we can obtain 
# zero largest coin + 1 largest coin + 2 largest coin to ( amount // largest_coin ) 
# after that, you move down to the lesser coin
# use separate functions
def coins(amount, change):
	return makeChange(amount, change, 0)

	def makeChange(total,change, index):
		coin = change[index]
		
		if index == len(change) - 1:
			remaining = total % coin
			if remaining == 0:
				return 1
		ways = 0
		
		amount = 0
		while amount <= total:
			ways += makeChange(total - amount, change, index + 1)
 			amount += coin
		return ways
			 
		
		
	
