class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        
        for i in range(n) :
            if nums[i] == 0 :
                continue
            if dp[-1] == 1 :
                return True
            
            if dp[i] == 1 :
                for j in range(1, nums[i]+1) :
                    if i+j < n :
                        dp[i+j] = 1
                    else :
                        break
                    
        return dp[-1] == 1