class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        
        # ...?
        prefix_sum = [[0] * COL for _ in range(ROW)]
        for x in range(ROW):
            for y in range(COL):
                left = prefix_sum[x][y - 1] if y > 0 else 0
                top = prefix_sum[x - 1][y] if x > 0 else 0
                top_left = prefix_sum[x - 1][y - 1] if x > 0 and y > 0 else 0
                prefix_sum[x][y] = left + top - top_left + matrix[x][y]
        
        res = 0
        for r1 in range(ROW):
            for r2 in range(r1, ROW):
                counter = {}
                for col in range(COL):
                    top = prefix_sum[r1 - 1][col] if r1 > 0 else 0
                    curr_sum = prefix_sum[r2][col] - top
                    if curr_sum == target:
                        res += 1
                    if curr_sum - target in counter:
                        res += counter[curr_sum - target]
                    counter[curr_sum] = counter.get(curr_sum, 0) + 1

        return res