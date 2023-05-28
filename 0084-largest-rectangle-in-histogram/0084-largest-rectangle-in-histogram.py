class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # dp같이 생기긴 했는데
        # dp[i]를 i에서 시작해서 가장 큰 너비라고 하면..?
        # 근데 각 위치마다 높이를 알아야 함..
        # 가장 간단한 방법은 이중 loop 돌면서 다 계산하는 것..
        # 아.. monotonic stack..?
        ans = 0
        stack = [] # stack에는 index를 넣어줌.
        
        # 코너 케이스 처리 위해 마지막에 0 추가...
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, w*h)
            stack.append(i)
        
        return ans