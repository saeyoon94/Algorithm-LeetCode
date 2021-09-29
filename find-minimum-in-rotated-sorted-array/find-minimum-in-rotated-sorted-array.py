class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        
        minimun = 5001
        
        while start <= end :
            min_element = min(nums[start], nums[mid], nums[end])
            if min_element ==   nums[mid] :
                if minimun > nums[mid] : 
                    minimun = nums[mid]
                if nums[start] < nums[end] :
                    start = mid +1
                else :
                    end = mid - 1
            elif min_element == nums[end] :
                if minimun > nums[end] :
                    minimun = nums[end]
                start = mid + 1
            else :
                if minimun > nums[start] :
                    minimun = nums[start]
                end = mid - 1
            mid = (start + end) // 2
                
        return minimun
        