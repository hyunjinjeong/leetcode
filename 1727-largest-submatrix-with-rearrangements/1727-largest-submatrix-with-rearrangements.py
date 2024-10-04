class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 뭔가 규칙이 있을텐데
        # 힌트를 보니 column마다 연속된 1의 갯수를 저장하고 정렬하면 됨
        # 그리고 row 단위로 정렬해서 계산..
        # 이게 어케 medium이지
        M, N = len(matrix), len(matrix[0])
        res = 0

        prev_heights = [0] * N
        for r in range(M):
            heights = matrix[r][:]
            for c in range(N):
                if heights[c] == 1:
                    heights[c] += prev_heights[c]
            
            sorted_heights = sorted(heights, reverse=True)
            for c in range(N):
                res = max(res, sorted_heights[c] * (c + 1))
            
            prev_heights = heights

        return res