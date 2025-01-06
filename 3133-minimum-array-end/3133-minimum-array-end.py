class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # 그러니까 nums의 조건은
        # 1. 길이가 n이고
        # 2. strictly increasing이어야 하고
        # 3. 모든 값을 AND하면 x가 나와야 함
        # 이 때 nums[n - 1]이 최솟값을 찾아야 함
        
        # 이건 TLE...
        # curr = x
        # for i in range(n - 1):
        #     curr = (curr + 1) | x
        
        # return curr

        curr = x
        n -= 1
        mask = 1

        while n > 0:
            if (mask & x) == 0:
                curr |= (n & 1) * mask
                n >>= 1
            mask <<= 1
        
        return curr