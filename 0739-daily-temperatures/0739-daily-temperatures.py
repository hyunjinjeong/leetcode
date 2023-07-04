class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack 활용하면 될 듯..?
        ans = [0] * len(temperatures)

        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_index = stack.pop()
                ans[prev_index] = index - prev_index
            
            stack.append(index)
        
        return ans
