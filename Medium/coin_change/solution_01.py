class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        N = len(coins) + 1
            
        dp = [[0] * (amount + 1) for _ in range(N)]
    
        for i in range(N): dp[i][0] = 1
            
        for i in range(1,N): 
            
            for j in range(amount+1):
                
                without_curr_coin = (dp[i-1][j] if i > 0 else 0)
                
                with_curr_coin = (dp[i][j - coins[i-1]] if j >= coins[i-1] else 0)
                
                dp[i][j] = (without_curr_coin + with_curr_coin)
              
        return dp[-1][-1]

