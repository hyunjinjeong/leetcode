class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # largest subset이라는게 숫자의 합이 아니고 subset의 갯수를 말함
        # 일단 decision tree.. 느낌으로 풀어보자
        # i번째가 있으면 i를 포함하거나, 포함하지 않거나.
        # 반대로 그냥 전체 subset을 다 구해서 조건에 맞는 subset들만 필터링해서 보면 됨
        # TLE가 뜨는데.. DP인 것 같음. 어떻게 DP로 전환하지. curr를 안 쓰도록 해보자.

        @cache
        def dfs(i, m_left, n_left):
            if i == len(strs) or m_left <= 0 and n_left <= 0:
                return 0

            if self.zeros[i] > m_left or self.ones[i] > n_left:
                return dfs(i + 1, m_left, n_left)
            
            pick = 1 + dfs(i + 1, m_left - self.zeros[i], n_left - self.ones[i])
            not_pick = dfs(i + 1, m_left, n_left)

            return max(pick, not_pick)
        
        self.ones = [0] * len(strs)
        self.zeros = [0] * len(strs)
        for i in range(len(strs)):
            for c in strs[i]:
                if c == "1":
                    self.ones[i] += 1
                else:
                    self.zeros[i] += 1
        
        return dfs(0, m, n)