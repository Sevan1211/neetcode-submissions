class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        result = []
        greatest = -1

        for num in arr[::-1]:
            result.append(greatest)

            greatest = max(greatest, num)
        
        return result[::-1]

