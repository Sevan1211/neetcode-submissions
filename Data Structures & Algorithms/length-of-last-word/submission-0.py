class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean = s.split()
        return len(clean[-1])