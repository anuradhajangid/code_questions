#https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        subdict = collections.Counter(t)
        sdict = {}
        minwindowlen = inf
        minwindow = [-1, -1]
        start = 0
        found = 0
        if len(s) < len(t) or len(s) == 0:
            return ""
        for end in range(len(s)):
            if s[end] in subdict:
                sdict[s[end]] = 1 + sdict.get(s[end], 0)

            if s[end] in subdict and sdict[s[end]] == subdict[s[end]]:
                found += 1

            while found == len(subdict):
                if (end - start + 1) < minwindowlen:
                    minwindowlen = end-start+1
                    minwindow = [start, end]
                if s[start] in subdict:
                    sdict[s[start]] = sdict.get(s[start], 1) - 1

                if s[start] in subdict and sdict[s[start]] < subdict[s[start]]:
                    found -= 1

                start += 1
        
        #print(minwindow, minwindowlen)        
        return s[minwindow[0]: minwindow[1]+1] if minwindowlen != inf else ""
                    

                

            