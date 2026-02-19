from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False 
        CS,CT=defaultdict(int),defaultdict(int)
        for i in range(len(s)):
            CS[s[i]]=1 + CS[s[i]]
            CT[t[i]]=1 + CT[t[i]]
        for c in s:
            if CS[c]!=CT[c]:
                return False
        return True       




        
        