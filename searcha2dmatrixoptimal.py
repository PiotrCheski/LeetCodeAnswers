#O(log(m*n))
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // cols][mid % cols]
            print(mid_element)
            
            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

                
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))