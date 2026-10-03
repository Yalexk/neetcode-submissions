class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        # first do a binary search to find which row to look in
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            # print(matrix[mid][0])
            # print(matrix[mid][-1])
            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else:
                row = mid
                break

        if row is None: return False

        lo, hi = 0, len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            # print(matrix[row][mid])
            if target == matrix[row][mid]:
                return True
            
            if target < matrix[row][mid]:
                hi = mid - 1
            else: 
                lo = mid + 1
        
        return False