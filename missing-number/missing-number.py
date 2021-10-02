class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        
        expected = max_num * (max_num+1) // 2
        
        return expected - sum(nums)