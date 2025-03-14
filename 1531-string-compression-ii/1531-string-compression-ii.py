class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 이거 결국 pick & not pick DP네
        
        @cache
        def dfs(i, char, count, left):
            if left < 0:
                return 100
            if i == len(s):
                return 0

            not_pick = dfs(i + 1, char, count, left - 1) # delete

            if s[i] == char:
                pick = dfs(i + 1, char, count + 1, left) + (1 if count in (1, 9, 99) else 0)
            else:
                pick = dfs(i + 1, s[i], 1, left) + 1
            
            return min(not_pick, pick)
        
        return dfs(0, "", 0, k)