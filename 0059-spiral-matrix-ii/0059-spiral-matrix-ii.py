class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        up_bound = 0
        down_bound = n - 1
        left_bound = 0
        right_bound = n - 1

        curr = 1
        while curr <= n ** 2:
            for i in range(left_bound, right_bound + 1):
                res[up_bound][i] = curr
                curr += 1
            up_bound += 1

            for i in range(up_bound, down_bound + 1):
                res[i][right_bound] = curr
                curr += 1
            right_bound -= 1

            for i in range(right_bound, left_bound - 1, -1):
                res[down_bound][i] = curr
                curr += 1
            down_bound -= 1

            for i in range(down_bound, up_bound - 1, -1):
                res[i][left_bound] = curr
                curr += 1
            left_bound += 1
        
        return res
