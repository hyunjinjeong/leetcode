class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # row의 패턴을 찾는 것.. 1100이나 0011이나 같은 패턴임
        # 그리고 0번 뒤집는 경우엔 기존 row가 모두 1이나 0인 개수를 세면 될 듯
        M, N = len(matrix), len(matrix[0])
        
        res = 0
        # find the rows that have all values equal
        for row in range(M):
            prev_num = -1
            is_all_equal = True
            for col in range(N):
                if prev_num == -1:
                    prev_num = matrix[row][col]
                elif matrix[row][col] != prev_num:
                    is_all_equal = False
                    break
            if is_all_equal:
                res += 1
        
        # find the rows with the same pattern
        patterns = collections.defaultdict(int)
        for row in range(M):
            pattern = "a"
            char = "a"
            for col in range(1, N):
                if matrix[row][col] == matrix[row][col - 1]:
                    pattern += char
                else:
                    char = "b" if char == "a" else "a"
                    pattern += char
            patterns[pattern] += 1
        
        res = max(res, max(patterns.values()))
        return res
