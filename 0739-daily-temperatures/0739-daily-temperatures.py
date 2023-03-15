class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # naive 솔루션은 자기보다 오른쪽에 있는거 다 찾는거고.. O(n^2)임.
        # 당연히 이건 안 될거고..
        # 투 포인터? dp?
        # 아 monotonic stack이란게 있다.
        
        ans = [0] * len(temperatures)
        
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return ans