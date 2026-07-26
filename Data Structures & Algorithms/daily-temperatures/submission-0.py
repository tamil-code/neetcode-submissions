class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack=[]
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            num = temperatures[i]
            while min_stack and num > temperatures[min_stack[-1]]:
                index = min_stack.pop()
                res[index] = i-index
            min_stack.append(i)
        return res
        