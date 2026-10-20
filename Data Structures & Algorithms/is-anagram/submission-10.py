class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            elif ch in freq:
                freq[ch] -= 1

        for ch in freq:
            if freq[ch] > 0:
                return False
        return True
            
