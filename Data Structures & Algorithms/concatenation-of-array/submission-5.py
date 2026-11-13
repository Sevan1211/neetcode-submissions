class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (2 * len(nums))


        for i, num in enumerate(nums):
            result[i] = result[i + len(nums)] = num
        
        return result