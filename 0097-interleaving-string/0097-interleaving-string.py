class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp...
        # 엣지 케이스
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}

        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                dp[(i1, i2)] = True
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            use_s1, use_s2 = False, False
            if i1 < len(s1) and s1[i1] == s3[i1+i2]:
                use_s1 = dfs(i1 + 1, i2)
            if i2 < len(s2) and s2[i2] == s3[i1+i2]:
                use_s2 = dfs(i1, i2 + 1)
            
            dp[(i1, i2)] = use_s1 or use_s2
            return dp[(i1, i2)]
        
        return dfs(0, 0)