class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [0] * (len(s))
        for w in wordDict :
            if self.is_prefix(s, w) :
                dp[len(w)-1] = 1
        
        
        for i in range(1, len(dp)) :
            for w in wordDict :
                n = len(w)
                if n <= i and dp[i-n] == 1 and self.is_prefix(s[i-n+1:], w) :
                    dp[i] = 1
        
        return dp[-1]
            

    def is_prefix(self, w1, w2) :
        if len(w1) < len(w2) :
            return False
        
        n = len(w2)
        return w1[:n] == w2