class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            elif freq[ch] > 0:
                freq[ch] -= 1
        
        for key, value in freq.items():
            if value > 0:
                return False
        return True