class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_set = set()
        c_set = set()
        
        r, c = len(matrix), len(matrix[0])
        
        for i in range(r) :
            for j in range(c) :
                if matrix[i][j] == 0 :
                    r_set.add(i)
                    c_set.add(j)
                    
        for i in range(r) :
            for j in range(c) :
                if i in r_set or j in c_set :
                    matrix[i][j] = 0