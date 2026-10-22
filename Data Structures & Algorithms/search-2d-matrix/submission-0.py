class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arr in matrix:
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2

                if target > mid:
                    l = mid + 1
                elif target < mid:
                    r = mid -1
                else:
                    return True
        return False