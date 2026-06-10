class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                largest = max(current, largest)
            else:
                current = 0
        return largest