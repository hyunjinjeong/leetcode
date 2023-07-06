class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        
        # monotonic stack 사용.
        # 마지막에 남은 원소들 모두 계산 위해 0 추가...
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                # stack[-1]이 h보다 작은 첫번쨰 원소니까
                # 가로 범위는 stack[-1]+1 ~ i-1
                # 즉 (i-1) - (stack[-1]+1) + 1 == i - stack[-1] - 1
                # 그래서 i - stack[-1] - 1이 w가 됨.
                # 그리고 stack이 비어 있으면 왼쪽이 모두 h보다 높은 거니까 i...
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, w*h)
            stack.append(i)
        
        return ans