class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        temp_nums = copy.deepcopy(nums)
        temp_nums.sort()
        
        answers = []
        result = []
        
        while start < end :
            now = temp_nums[start] + temp_nums[end]
            if now == target :
                answers = [temp_nums[start], temp_nums[end]]
                break
            
            elif now < target :
                start += 1
            else :
                end -= 1
                
        for i in range(len(nums)) :
            if nums[i] in answers :
                result.append(i)
        
        return result
        
        