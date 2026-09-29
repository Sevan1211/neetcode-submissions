class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + '#' + string
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        for i, ch in enumerate(s[0:len(s) -1]):
            if ch.isnumeric() and s[i + 1] == '#':
                res.append(s[i + 2: i + 2 + int(ch)])
        return res 

