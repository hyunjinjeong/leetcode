class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)

        counter = collections.defaultdict(int)
        for i in range(N):
            for j in range(N):
                num = grid[i][j]
                counter[num] += 1
        
        res = [-1, -1]
        for num in range(1, N ** 2 + 1):
            if counter[num] == 2:
                res[0] = num
            elif counter[num] == 0:
                res[1] = num
        
        return res