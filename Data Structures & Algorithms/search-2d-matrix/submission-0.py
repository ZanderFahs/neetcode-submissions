class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        t = 0
        b = r - 1
        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        if not t <= b:
            return False
        row = (t + b ) // 2
        l = 0
        r = c - 1
        while l <= r:
            mid = (r+l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False