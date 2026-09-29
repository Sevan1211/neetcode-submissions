import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            result.append(math.prod(nums[0:i]) * math.prod(nums[i + 1:]))
        return result