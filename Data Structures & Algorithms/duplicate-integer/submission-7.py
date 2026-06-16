class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i, num in enumerate(nums[:-1]):
            if nums[i] == nums[i+1]:
                return True
        return False