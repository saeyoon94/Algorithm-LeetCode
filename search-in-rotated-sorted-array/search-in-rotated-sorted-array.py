class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 1 :
            if nums[0] == target :
                return 0
            else :
                return -1
        
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        
        minimun = 10001
        minindex = -1
        
        
        while start <= end :
            min_element = min(nums[start], nums[mid], nums[end])
            if min_element ==   nums[mid] :
                if minimun > nums[mid] : 
                    minimun = nums[mid]
                    minindex = mid
                if nums[start] < nums[end] :
                    start = mid +1
                else :
                    end = mid - 1
            elif min_element == nums[end] :
                if minimun > nums[end] :
                    minimun = nums[end]
                    minindex = end
                start = mid + 1
            else :
                if minimun > nums[start] :
                    minimun = nums[start]
                    minindex = start
                end = mid - 1
            mid = (start + end) // 2
        
        
        
        if minindex == 0 :
            start = 0
            end = len(nums) - 1
        
        elif nums[0] <= target <= nums[minindex-1] :
            start = 0
            end = minindex-1
        else :
            start = minindex
            end = len(nums) - 1
        
        print(start, end, minindex)
        while start <= end :
            mid = (start + end) // 2
            
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                start = mid + 1
            else :
                end = mid - 1
        return -1
            
        
        