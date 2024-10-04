class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 뭔가 규칙이 있을텐데
        # 힌트를 보니 column마다 연속된 1의 갯수를 저장하고 정렬하면 됨
        # 그리고 row 단위로 정렬해서 계산..
        # 이게 어케 medium이지
        M, N = len(matrix), len(matrix[0])
        res = 0

        prev_row = [0] * N
        for r in range(M):
            row = matrix[r][:]
            for c in range(N):
                if row[c] == 1:
                    row[c] += prev_row[c]
            
            sorted_row = sorted(row, reverse=True)
            height = sorted_row[0]
            
            for c in range(N):
                height = min(sorted_row[c], height)
                res = max(res, height * (c + 1))
            
            prev_row = row

        return res