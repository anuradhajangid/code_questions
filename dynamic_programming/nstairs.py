import datetime

def staircase(n, m):
    # brute force method 
    #return  bruteForce(n,m)
    # dynamic programing top-down approach
    return dynamicTopDown(n,m)

#Time complexity  = m**n
#Space complexity = constant
def bruteForce(n,m):
    results = [0]
    def recursive(cLocation, cPath):
        cPath.append(cLocation)
        if cLocation == n:
            results[0] += 1
            return
        for i in range(1,m+1):
            if cLocation + i <=n:
                recursive(cLocation+i,cPath)
        return 
    recursive(0,[])
    return results[0]

#TimeComplexity = m * n
# Space Complexity = n
def dynamicTopDown(n,m):
    memo = {}
    def _recursive(n, m, memo):
        # base case
        if n == 0:
            return 1
        # check in memo
        if n in memo:
            return memo[n]
        ways = 0
        for i in range(1, m+1):
            if i <= n:
                ways += _recursive(n-i,m,memo)
        memo[n] = ways
        return ways
    return _recursive(n, m, memo)
assert staircase(1, 1) == 1
assert staircase(2, 1) == 1
assert staircase(4, 2) == 5
start = datetime.datetime.now()
assert staircase(12, 3)	 == 927
end = datetime.datetime.now()
print((end-start))