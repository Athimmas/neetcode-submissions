class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT,stackI = stack[-1]
                res[stackI] = i - stackI
                stack.pop()

            stack.append([t,i])

        return res 