class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for ch in s[::-1]:
            if ch.isalnum() == True:
                count += 1
            
            if ch.isalnum() == False and count > 0:
                break 
        return count