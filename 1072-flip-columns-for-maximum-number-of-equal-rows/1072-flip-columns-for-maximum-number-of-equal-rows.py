class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # row의 패턴을 찾는 것.. 1100이나 0011이나 같은 패턴임
        M, N = len(matrix), len(matrix[0])
        
        # find the rows with the same pattern
        patterns = collections.defaultdict(int)
        for row in range(M):
            pattern = ["a"]
            for col in range(1, N):
                if matrix[row][col] == matrix[row][col - 1]:
                    pattern.append(pattern[-1])
                else:
                    pattern.append("b" if pattern[-1] == "a" else "a")
            patterns["".join(pattern)] += 1

        return max(patterns.values())
