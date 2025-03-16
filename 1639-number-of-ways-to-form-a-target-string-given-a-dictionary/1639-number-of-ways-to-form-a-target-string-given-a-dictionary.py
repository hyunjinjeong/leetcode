class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # 누가봐도 DP인데
        # 상태가 3개 필요한가? 
        # words 인덱스랑 word 인덱스 그리고 pick한 개수? target은 정해져 있으니까 개수만 세면 될 듯
        # len(words) = N
        # len(words[0]) = L
        # len(target) = T
        # 일 때 O(NLT)가 걸리겠다
        # words는 그냥 매번 루프를 돌면 상태는 따로 필요하지 않을 듯?

        # 답은 맞는데 TLE가 뜬다.
        MOD = 10 ** 9 + 7

        frequency = [[0] * 26 for _ in range(len(words[0]))]
        for word in words:
            for i in range(len(word)):
                frequency[i][ord(word[i]) - ord("a")] += 1

        @cache
        def dfs(i, target_index):
            if target_index == len(target):
                return 1
            if i == len(words[0]):
                return 0
            
            res = 0

            # for word in words:
            #     if word[i] == target[target_index]:
            #         # 여기가 똑같은 dfs(i + 1, target_index + 1)을 계쏙 호출하니까 그냥 곱하면 될 듯?
            #         res = (res + dfs(i + 1, target_index + 1)) % MOD # pick

            freq = frequency[i][ord(target[target_index]) - ord("a")]
            res = (res + freq * dfs(i + 1, target_index + 1) % MOD) % MOD # pick
            res = (res + dfs(i + 1, target_index)) % MOD # skip

            return res
        
        return dfs(0, 0)