class Solution:
    def romanToInt(self, s: str) -> int:
        dt = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        ans = dt[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if dt[s[i]] < dt[s[i + 1]]:
                ans -= dt[s[i]]
            else:
                ans += dt[s[i]]
        
        return ans
