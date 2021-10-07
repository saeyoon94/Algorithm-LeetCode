class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        
        def rotate(x1,y1,x2,y2,matrix,result) :
            
            if x1 != x2 and y1 != y2 :
                for y in range(y1, y2) :
                    result.append(matrix[x1][y])

                for x in range(x1, x2) :
                    result.append(matrix[x][y2])

                for y in range(y2, y1, -1) :
                    result.append(matrix[x2][y])

                for x in range(x2, x1, -1) :
                    result.append(matrix[x][y1])
            elif x1 == x2 :
                result += matrix[x1][y1:y2+1]
                
            else :
                for x in range(x1, x2+1) :
                    result.append(matrix[x][y1])
                

            #result.append(matrix[x1][y1])
        
        x1,y1,x2,y2 = 0,0,len(matrix)-1,len(matrix[0])-1
        
        if y2 == 0 :
            return [i[0] for i in matrix]
        
        
        while x1<=x2 and y1<=y2 :
            rotate(x1,y1,x2,y2,matrix,result)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
            
        return result
                
            