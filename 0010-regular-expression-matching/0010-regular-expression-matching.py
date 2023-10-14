class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # * 앞의 캐릭터를 사용하는지 안하는지.
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dfs(i, j + 2) or match and dfs(i + 1, j)
            else:
                ans = dfs(i + 1, j + 1) if match else False
            
            cache[(i, j)] = ans
            return ans
        
        return dfs(0, 0)