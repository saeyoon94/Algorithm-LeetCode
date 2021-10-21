class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        
        
        def rotation(matrix, i, n):
            if n - 2 * i <= 1:
                return False

            result = []

            for a in range(i, n - i):
                result.append(matrix[i][a])

            for a in range(i + 1, n - i):
                result.append(matrix[a][n - i - 1])

            for a in range(n - i - 2, i - 1, -1):
                result.append(matrix[n - i - 1][a])

            for a in range(n - i - 2, i, -1):
                result.append(matrix[a][i])


            result = result[-(n - 1 -2*i):] + result[:-(n - 1 -2*i)]
            result = result[::-1]

            for a in range(i, n - i):
                matrix[i][a] = result.pop()

            for a in range(i + 1, n - i):
                matrix[a][n - i - 1] = result.pop()

            for a in range(n - i - 2, i - 1, -1):
                matrix[n - i - 1][a] = result.pop()

            for a in range(n - i - 2, i, -1):
                matrix[a][i] = result.pop()

            return True
        
        while True :
            if not rotation(matrix, i, n) :
                break
            i += 1