class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {0:0}
        def topDown(amount, coins):
            
            if amount == 0: return cache[amount]
            
            if amount in cache: return cache[amount]
            
            cache[amount] = float('inf')
            
            for coin in coins:
                
                if amount - coin >= 0:
                    
                    temporary_minimum = topDown(amount - coin, coins) + 1
                    cache[amount] = min(cache[amount], temporary_minimum)
                
                else:
                    continue
            return cache[amount]
        
        
        ans = topDown(amount, coins)
        
        return ans if ans != float('inf') else -1
###Top down approaach
###Run time 0 ( S * n )
###Space o ( n )  (maximum stack depth)
