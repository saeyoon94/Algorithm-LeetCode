class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.factorial(m+n-2) // (self.factorial(m-1)*self.factorial(n-1))
        
    
        
    def factorial(self, m) :
        result = 1
        
        for i in range(2, m+1) :
            result *= i
        return result
        