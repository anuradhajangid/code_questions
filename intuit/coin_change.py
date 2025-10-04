from typing import List
class Solution:
    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
        memo ={}
        def helper(current_amount):
            if current_amount == 0:
                return 0
            if current_amount < 0:
                return -1
            if current_amount in memo:
                return memo[current_amount]
            min_count = float("inf")
            for coin in coins:
                res = helper(current_amount-coin)
                if res != -1:
                    min_count = min(min_count, res)
            memo[current_amount] = min_count if min_count != float("inf") else -1
            return memo[current_amount]
        return helper(amount)

    def coinChangeBottomUp(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount +1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != float("inf"):
                    dp[i] = min(dp[i], 1+ dp[i-coin])
        
        return dp[amount] if dp[amount] != float("inf") else -1