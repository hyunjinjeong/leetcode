class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 뭔가 규칙이 있을텐데
        # 힌트를 보니 column마다 연속된 1의 갯수를 저장하고 정렬하면 됨
        # 그리고 row 단위로 정렬해서 계산..
        # 이게 어케 medium이지
        M, N = len(matrix), len(matrix[0])

        for c in range(N):
            for r in range(1, M):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]
        
        res = 0
        for r in range(M):
            curr_row = sorted(matrix[r], reverse=True)
            height = curr_row[0]
            for c in range(N):
                height = min(curr_row[c], height)
                res = max(res, height * (c + 1))

        return res