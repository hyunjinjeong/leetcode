class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = collections.Counter(t)

        ans = (0, 0)
        ans_count = 0

        left = 0
        for right, c in enumerate(s):
            if t_counter[c] > 0:
                ans_count += 1
            t_counter[c] -= 1

            while ans_count == len(t):
                # (0, 0)은 엣지 케이스...
                if right - left + 1 < ans[1] - ans[0] or ans == (0, 0):
                    ans = (left, right + 1)

                t_counter[s[left]] += 1
                if t_counter[s[left]] > 0:
                    ans_count -= 1

                left += 1
        
        return s[ans[0]:ans[1]]