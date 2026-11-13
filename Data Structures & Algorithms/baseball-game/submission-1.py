class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        score = 0


        for i, o in enumerate(operations):
            if o.isnumeric():
                result.append(int(o))
            elif o == '+':
                result.append(result[-1] + result[-2])
            elif o == 'D':
                result.append(result[-1] * 2)
            else:
                result.pop()
        return sum(result)