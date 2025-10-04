#https://leetcode.com/problems/valid-palindrome-iii?envType=problem-list-v2&envId=7p59281
class Solution:
    def isValidPalindrom(self, s:str, k:int) -> bool:
        self.string = s

        memo = {}

        def helper(i, j, k):
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            elif not k:
                memo[(i,j,k)] = self.isPalindrom(i,j)
            else:
                while i < j:
                    if self.string[i] != self.string[j]:
                        memo[(i,j,k)] = helper(i+1,j,k-1) or helper(i,j+1,k-1)
                        return memo[(i,j,k)]
                    i+=1
                    j-=1
                memo[(i,j,k)] = True
            return memo[(i,j,k)]

        return helper(0,len(self.string)-1, k)
    
    def isPalindrom(self, i,j):
        while i < j:
            if self.string[i] != self.string[j]:
                return False
            i += 1
            j -=1
        return False

