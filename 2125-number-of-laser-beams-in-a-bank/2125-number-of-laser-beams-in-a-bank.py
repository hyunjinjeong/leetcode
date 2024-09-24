class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # row마다 security device의 수를 센 다음에
        # 각각 m * n이런 식으로 곱하면 되지 않으려나?
        M, N = len(bank), len(bank[0])
        
        res = 0
        prev, curr = 0, 0

        for r in range(M):
            for c in range(N):
                if bank[r][c] == "1":
                    curr += 1
            
            if curr > 0:
                res += prev * curr
                prev, curr = curr, 0
        
        return res