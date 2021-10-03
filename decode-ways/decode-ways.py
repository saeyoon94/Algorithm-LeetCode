class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0" :
            return 0
        
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 
        
        
        
        
        for i in range(2, len(s)+1) :
            dp[i] = (dp[i-1] if s[i-1] != "0" else 0) + (dp[i-2] if (s[i-2] != '0') and ('00' < s[i-2]+s[i-1] <= '26') else 0)
            
        return dp[-1]
            
            