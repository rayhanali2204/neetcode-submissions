class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # 1. Binary Search to find the correct ROW
        top_row, bot_row = 0, ROWS - 1
        while top_row <= bot_row:
            row = (top_row + bot_row) // 2
            
            # Target is greater than the biggest element in this row
            if target > matrix[row][-1]:
                top_row = row + 1
            # Target is smaller than the smallest element in this row
            elif target < matrix[row][0]:
                bot_row = row - 1
            else:
                break # Found the correct row!
        
        # If pointers cross, the row doesn't exist
        if not (top_row <= bot_row):
            return False
            
        # 2. Standard 1D Binary Search inside that specific row
        row = (top_row + bot_row) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return False
