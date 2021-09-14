class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        min_val = prices[0]
        max_gap = 0
        
        for price in prices[1:] :
            if price < min_val :
                min_val = price
            
            if price-min_val > max_gap :
                max_gap = price-min_val
                
        return max_gap