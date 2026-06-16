
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch in freq and freq[ch] > 0:
                freq[ch] -= 1
            else:
                return False
        return True if sum(freq.values()) == 0 else False