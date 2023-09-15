class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        maxlength = 0
        start = 0
        for end in range(len(s)):
            if s[end] in frequency:
                frequency[s[end]] +=1
            else:
                frequency[s[end]] = 1
            if not ((end - start + 1) - max(frequency.values()) <=k):
                while ((end-start+1) - max(frequency.values())) > k:
                    print(frequency[s[start]])
                    frequency[s[start]] -=1
                    if frequency[s[start]] ==0:
                        del frequency[s[start]]
                    start +=1
            maxlength = max((end-start+1), maxlength)
        return  maxlength
        