class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                res[row][col] = original[row * n + col]
        return res