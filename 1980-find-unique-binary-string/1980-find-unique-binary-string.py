class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n <= 16이니까 모든 조합을 다 봐도 되려나?
        # 2^16이면.. 많긴 하다.
        def to_binary_string(n):
            res = []
            while n:
                if n % 2 == 1:
                    res.append("1")
                else:
                    res.append("0")
                n = n // 2
            
            while len(res) < N:
                res.append("0")
            
            res.reverse()
            return "".join(res)
        
        def to_int(s):
            res = 0
            for c in s:
                curr = 1 if c == "1" else 0
                res = res * 2 + curr
            return res
        
        N = len(nums)
        limit = N ** 2 if N > 1 else 2
        num_set = set([to_int(num) for num in nums])
        
        for i in range(limit):
            if i not in num_set:
                return to_binary_string(i)
            
        # 1이면 0, 1
        # 2면 0, 1, 2, 3
        # 3이면 0, 1, 2, 3, 4, 5, 6, 7...