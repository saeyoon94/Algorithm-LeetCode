class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        water = (len(height)-1) * min(height[0], height[-1])
        
        start = 0
        end = len(height)-1
        
        if height[start] < height[end] :
            start += 1
        else :
            end -= 1
        
        while start < end :
            temp = (end-start) * min(height[start], height[end])
            if temp > water :
                water = temp
        
            if height[start] < height[end] :
                start += 1
            else :
                end -= 1
            
        return water
            
        
        
        
        
        
        
        
        
        
        
        
        
        
            