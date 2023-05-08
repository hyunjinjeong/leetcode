class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = collections.Counter(t)
        # 1. 우선 substring을 찾을 때까지 r을 늘리다가 (끝까지 가도 없으면 "" 리턴)
        # 2. 찾고 나면 또 조건을 만족할 때까지 l을 늘려주면 된다!
        # 3. l을 늘리다가 조건에서 벗어나면 다시 1-2번 반복.
        ans = ""
        l = 0
        for r, c in enumerate(s):
            if c in t_counter:
                t_counter[c] -= 1

            while all([v <= 0 for v in t_counter.values()]):
                if r+1-l < len(ans) or ans == "":
                    ans = s[l:r+1]
                
                if s[l] in t_counter:
                    t_counter[s[l]] += 1
                l += 1
                
        return ans
        