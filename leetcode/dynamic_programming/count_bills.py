from typing import List
class Solution:
    def count_bills_recursive(self,bills,amount):
        """
        TC: O(n**C)
        SC = O(1)
        """
        def _countways(bills, amount, maximum):
            if amount == 0:     # base case 1
                return 1
            ways = 0
            # iterate over bills
            for bill in bills:    
                # to avoid repetition of similar sequences, use bills smaller than maximum
                if bill <= maximum and amount - bill >= 0:  
                # notice how bill becomes maximum in recursive call    
                    ways += _countways(bills, amount-bill, bill)  
            return ways
        return _countways(bills, amount, max(bills))
    
    def count_bills_memoization(self,bills, amount):
        """
        TC: O(n*C)
        SC = O(nC)
        """
        memo = {}
        def _countways(bills, amount, maximum, memo):
            if amount == 0:
                return 1
            if (amount, maximum) in memo:
                return memo[amount, maximum]
            ways = 0
            for bill in bills:
                if bill <= maximum and amount -bill >=0:
                    ways += _countways(bills, amount-bill, bill, memo)
            memo[(amount, maximum)] = ways
            return ways

        return _countways(bills, amount, max(bills), memo)

    def count_bills_tabulation(self,bills, amount):
        """
        TC: O(n**C)
        SC = O(n*C)
        """
        table = [[1 for _ in range(len(bills))] for _ in range(amount+1)]
        if amount  <= 0:
            return 0
        for amt in range(1, amount+1):
            for j in range(len(bills)):
                bill = bills[j]
                if amt - bill >= 0:
                    x = table[amt-bill][j]
                else:
                    x = 0
                if j >=1:
                    y = table[amt][j-1]
                else:
                    y = 0
                table[amt][j] = x + y
        return table[amount][len(bills) - 1]


assert Solution().count_bills_recursive([10,20], 30) == 2
assert Solution().count_bills_memoization([10,20], 30) == 2
assert Solution().count_bills_tabulation([10,20], 30) == 2