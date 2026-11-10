class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        curr = 0

        for num in nums:
            if num == 1 and curr == m:
                m += 1
                curr += 1
            elif num == 1:
                curr += 1
            else:
                curr = 0
        return m
