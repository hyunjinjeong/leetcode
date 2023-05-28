class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [] # stack에는 index를 넣어줌.
        
        # 코너 케이스 처리 위해 마지막에 0 추가...
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                # i가 h보다 낮은 오른쪽 첫번째, stack[-1]이 h보다 낮은 왼쪽 첫번째
                # 그래서 i - stack[-1] - 1은 사각형 길이가 됨.
                # 그리고 stack이 비어 있으면 왼쪽이 모두 h보다 높은 거니까 i...
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, w*h)
            stack.append(i)
        
        return ans