#daily temperaturs 



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stackind , stackval  = stack.pop()

                res[stackind] = ind - stackind

            stack.append((stackind, stackval))

        return res
