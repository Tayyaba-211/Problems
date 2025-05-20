
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)       # Number of rows
        n = len(matrix[0])    # Number of columns

        # Treat the 2D matrix as a 1D array for binary search
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n    # Map 1D index to 2D row
            col = mid % n     # Map 1D index to 2D column
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
