class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 일단 brute force로 해보자
        # i번째가 있다면 포함하거나, 포함하지 않거나 두 가지 경우의 수
        # 그럼 dfs
        # 이걸 dp로 발전시킬 수 있을 듯?

        def dfs(i, j, cache):
            if j == len(t): # j에서 끝까지 왔다는 건 subsequence
                return 1
            if i == len(s): # subsequence를 찾지 못함
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            ans = 0
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1, cache)
                ans += dfs(i + 1, j, cache)
            else:
                ans += dfs(i + 1, j, cache)
            
            cache[(i, j)] = ans
            return ans
                
        return dfs(0, 0, {})