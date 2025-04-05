class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        
        if k == 0:
            return res
        
        if k > 0:
            for i in range(N):
                for j in range(1, k + 1):
                    res[i] += code[(i + j) % N]
            return res

        if k < 0:
            for i in range(N):
                for j in range(1, -k + 1):
                    index = i - j if i - j >= 0 else N + i - j
                    res[i] += code[index]
            return res                